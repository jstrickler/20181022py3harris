#!/usr/bin/env python

from carddeck import CardDeck

class Dog():
    def bark(self):
        print("Woof! Woof!")

class JokerDeck(CardDeck, Dog):

    def _create_deck(self):
        super()._create_deck()
        for i in range(1, 3):
            joker = str(i), 'Joker'
            self._cards.append(joker)
