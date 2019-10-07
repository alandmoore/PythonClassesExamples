"""Competetive Guessing Game without Classes"""

import random


player1_name = input('Player 1, what is your name? ')
player1_score = 0
player1_guesses = 3

player2_name = input('Player 2, what is your name? ')
player2_score = 0
player2_guesses = 3

def get_guess(name, score, guesses, secret_number):
    while True:
        guess = input(f'{name}, what is your guess (1, 2, or 3)? ')
        if guess.isdigit():
            break

    if int(guess) == secret_number:
        score += 1
        print(f'*** You guessed it, {name}! ***')
    else:
        guesses -= 1
        print(f'Wrong guess, {name}!')
    return score, guesses

# Gameplay starts here
while player1_guesses > 0 or player2_guesses > 0:
    secret_number = random.randint(1, 3)
    if player1_guesses > 0:
        player1_score, player1_guesses = get_guess(
            player1_name, player1_score, player1_guesses, secret_number
        )
    if player2_guesses > 0:
        # Note the easy-to-make bug here and its impact
        player1_score, player2_guesses = get_guess(
            player2_name, player2_score, player2_guesses, secret_number
        )

# Game over, tally the winner
if player1_score > player2_score:
    print(f'Game over, {player1_name} won!')
elif player2_score > player1_score:
    print(f'Game over, {player2_name} won!')
else:
    print('Game over, nobody won :-(')
