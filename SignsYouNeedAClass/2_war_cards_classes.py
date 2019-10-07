"""War card game simulator with Classes"""

import random

class Card:

    ranks = ('Ace', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'Jack', 'Queen', 'King')
    suits = ('♣', '♠', '♡', '♢')

    @classmethod
    def make_deck(cls):
        return [
            cls(rank, suit) for rank in cls.ranks for suit in cls.suits
        ]

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = self.ranks.index(rank)

    def __str__(self):
        return f'the {self.rank} of {self.suit}'

    def __gt__(self, other):
        return self.value > other.value

# Start Game
deck = Card.make_deck()
random.shuffle(deck)

while deck:
    player1_card = deck.pop()
    player2_card = deck.pop()

    if player1_card > player2_card:
        print(f'Player 1 beat player 2 with {player1_card} against {player2_card}')
    elif player2_card > player1_card:
        print(f'Player 2 beat player 1 with {player2_card} against {player1_card}')
    else:
        print(f'Both players got a {player1_card.rank}, it is a tie!')
