import classik
from classik import Card
from classik import Positionable_Card
from classik import Unprintable_Card
card1=Card("T",Card.Suits[0]) 
card2=Unprintable_Card("T",Card.Suits[1]) 
card3=Positionable_Card("T",Card.Suits[2]) 
print("Texting object Card:") 
print(card1) 
print("\ntexting object Uprintable_Card:") 
print(card2) 
print("\ntec=texting object Positionable_Card:") 
print(card3) 
print("flip card down object Positiaonble_Caard.") 
card3.flip() 
print("texting object Positionable_Card") 
print(card3)