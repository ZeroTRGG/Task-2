import random
import sys

class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.name = str(self.rank) + " of " + self.suit

def create_deck():
    suit = [u'\u2660',u'\u2663',u'\u2665',u'\u2666']

    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    num = 2
    for i in suit:
        for x in rank:
            deck.append(Card(x, i, num))
            num = num + 1
        num = 2

    return sorted(deck, key=lambda k: random.random())

def deal_cards(deck):  
    x = 0
    i = 0
    player1 = []
    player2 = []
    while i < len(deck):
        if x == 0:
            player1.append(deck[i])
            x = 1
        else:
            player2.append(deck[i])
            x = 0
        i += 1
    return player1, player2

def game():
    pl1wins = 0
    pl2wins = 0
    while (pl1wins + pl2wins) <= 50: 
        deck = create_deck()
        players = deal_cards(deck)
        player1 = players[0]
        player2 = players[1]

        player1 = sorted(player1, key=lambda card: card.value)
        war = []

        turns = 0
        while len(player1) > 0 and len(player2) > 0:
            turns = turns + 1
            if (len(player1) + len(player2)) > 52:
                print("Oh NO!")
                sys.exit()
            war = []
            war.append(player1[0])
            war.append(player2[0])

            player1.remove(player1[0])
            player2.remove(player2[0])
            if war[0].value > war[1].value:
                i = 0
                n = len(war)
                while i < n:
                    player1.append(war[0])
                    war.remove(war[0])
                    i = i + 1

            elif war[0].value < war[1].value:
                i = 0
                n = len(war)
                while i < n:
                    player2.append(war[0])
                    war.remove(war[0])
                    i = i + 1

            elif war[0].value == war[1].value:
                if len(player1) == 0:
                    player1.append(war[0])
                    war.remove(war[0])
                    if player1[0].value == player2[0].value:
                        player1[0].value = 0
                if len(player2) == 0:
                    player2.append(war[1])
                    war.remove(war[1])
                    if player1[0].value == player2[0].value:
                        player2[0].value = 0
                while len(war) > 0:

                    i = 0
                    for i in range(3):
                        if len(player1) > 1:
                            war.append(player1[0])
                            player1.remove(player1[0])

                        if len(player2) > 1:   
                            war.append(player2[0])
                            player2.remove(player2[0])

                    if player1[0].value > player2[0].value:
                        war.append(player1[0])
                        war.append(player2[0])
                        player1.remove(player1[0])
                        player2.remove(player2[0])
                        i = 0
                        n = len(war)
                        while i < n:
                            player1.append(war[0])
                            war.remove(war[0])
                            i = i + 1      
                    elif player1[0].value < player2[0].value:
                        war.append(player1[0])
                        war.append(player2[0])
                        player1.remove(player1[0])
                        player2.remove(player2[0])
                        i = 0
                        n = len(war)
                        while i < n:
                            player2.append(war[0])
                            war.remove(war[0])
                            i = i + 1

        if len(player1) != 0:
            print("Player1 wins!")
            pl1wins = pl1wins + 1
        elif len(player2) != 0:
            print ("Player2 wins!")
            pl1wins = pl2wins + 1
    print(pl1wins + " versus " + pl2wins)
game()
