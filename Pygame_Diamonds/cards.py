import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Suit:
    def __init__(self, suit):
        self.suit = suit

    def create_suit(self):
        deck = [Card(self.suit, RANKS[i], VALUES[i]) for i in range(13)]
        return deck

    def shuffle_deck(self, deck):
        return random.shuffle(deck)
