import os
os.getcwd()
class Card: 
    """One gaming card""" 
    Ranks=["A","2","3","4","5","6","7", 
            "8","9","10","J","Q","K"] 
    #213 
    Suits=[u'\u2660',u'\u2663',u'\u2665',u'\u2666'] 
 
    def __init__(self,rank,suit): 
        self.rank=rank 
        self.suit=suit 
 
    def __str__(self): 
        rep=self.rank+self.suit 
        return rep 
class Hand: 
    """ Hand: Cads which lies on hand of one player""" 
    def __init__(self): 
        self.cards=[] 
 
    def __str__(self): 
        if self.cards: 
            rep="" 
            for card in self.cards: 
                rep+=str(card)+"\t" 
        else: 
            rep="<None>" 
        return rep 
    def clear(self): 
        self.cards=[] 
    def add(self,card): 
        self.cards.append(card) 
    def give(self,card,other_hand): 
        self.cards.remove(card) 
        other_hand.add(card) 
class Deck(Hand): 
    """Gaming cards""" 
    def populate(self): 
        for suit in Card.Suits: 
            for rank in Card.Ranks: 
                self.add(Card(rank,suit)) 
    def shuffle(self): 
        import random 
        random.shuffle(self.cards) 
    def deal(self,hands,per_hand=1): 
        for rounds in range(per_hand): 
            for hand in hands: 
                if self.cards: 
                    top_card=self.cards[0] 
                    self.give(top_card,hand) 
                else: 
                    print("Cannot put cards more:") 
class Unprintable_Card(Card): 
    """Card which we can not print""" 
    def __str__(self): 
        return "<can not texting>" 
class Positionable_Card(Card): 
    """Card which we can put with face down""" 
    def __init__(self,rank,suit,face_up=True): 
        super().__init__(rank,suit) 
        self.is_face_up=face_up 
    def __str__(self): 
        if self.is_face_up: 
            rep=super().__str__() 
        else: 
            rep="XX" 
        return rep 
    def flip(self): 
        self.is_face_up=not self.is_face_up 