"""War card game simulator without Classes"""

import random

deck = [
    'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'X♣', 'J♣', 'Q♣', 'K♣',
    'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'X♠', 'J♠', 'Q♠', 'K♠',
    'A♡', '2♡', '3♡', '4♡', '5♡', '6♡', '7♡', '8♡', '9♡', 'X♡', 'J♡', 'Q♡', 'K♡',
    'A♢', '2♢', '3♢', '4♢', '5♢', '6♢', '7♢', '8♢', '9♢', 'X♢', 'J♢', 'Q♢', 'K♢',
]

def compare_cards(card1, card2):
    card1_rank = card1[0]
    card2_rank = card2[0]
    rank_values = {'A': 1, 'X': 10, 'J': 11, 'Q': 12, 'K': 13}
    card1_value = rank_values.get(card1_rank) or int(card1_rank)
    card2_value = rank_values.get(card2_rank) or int(card2_rank)
    return card1_value > card2_value

#Start game
random.shuffle(deck)
while deck:
    player1_card = deck.pop()
    player2_card = deck.pop()

    if compare_cards(player1_card, player2_card):
        print(f'Player 1 beat player 2 with {player1_card} against {player2_card}')
    elif compare_cards(player2_card, player1_card):
        print(f'Player 2 beat Player 1 with {player2_card} against {player1_card}')
    else:
        print(f'Both players drew a {player1_card[0]}, it is a tie!')
