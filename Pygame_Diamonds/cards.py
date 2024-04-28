import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Suit:
    def __init__(self, suit):
        self.suit = suit

    def create_suit(self, suit, values):
        deck = [Card(suit, value) for value in values]
        return deck

    def shuffle_deck(self, deck):
        return random.shuffle(deck)