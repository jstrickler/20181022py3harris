#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Betty")
# CardDeck d1 = new CardDeck("Betty")
print(d1)
print(d1.get_dealer())

print(CardDeck.get_dealer(d1))

print(d1.dealer)

d1.dealer = 'Marsha'

print(d1.dealer)

try:
    d1.dealer = 123.456
except Exception as err:
    print(err)
else:
    print(d1.dealer)

print()
d1.shuffle()
print(d1.cards)
print(len(d1.cards))

hand = []
for i in range(5):
    hand.append(d1.draw())
print(hand)

j1 = JokerDeck('Bob')
print(j1)
j1.shuffle()
print(j1.cards)

j1.bark()

print(JokerDeck.mro())

print(len(j1))
print(d1)
