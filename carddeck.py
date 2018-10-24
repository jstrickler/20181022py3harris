#!/usr/bin/env python
import random

class CardDeck():
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    def get_dealer(self):
        return self._dealer


    @property
    def dealer(self):
        return self._dealer

    # dealer = property(dealer)

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop(0)

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        class_type = type(self)
        class_name = class_type.__name__
        return f"{class_name}({len(self)})"
