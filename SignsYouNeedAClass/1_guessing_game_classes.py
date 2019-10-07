"""Competetive Guessing Game with Classes"""

import random

class Player:

    def __init__(self, name):
        self.name = name
        self.guesses = 3
        self.score = 0

    def get_guess(self, secret_number):
        while True:
            guess = input(f'{self.name}, what is your guess (1, 2, or 3)? ')
            if guess.isdigit():
                break
        if int(guess) == secret_number:
            self.score += 1
            print(f'*** You guessed it, {self.name}! ***')
        else:
            self.guesses -= 1
            print(f'{self.name} guessed wrong!')

    def has_guesses(self):
        return self.guesses > 0

player1 = Player(input('Player 1, what is your name? '))
player2 = Player(input('Player 2, what is your name? '))

# Gameplay starts here
while player1.has_guesses() or player2.has_guesses():
    secret_number = random.randint(1, 3)
    if player1.has_guesses():
        player1.get_guess(secret_number)
    if player2.has_guesses():
        player2.get_guess(secret_number)

# Game Over, tally the winner
if player1.score > player2.score:
    print(f'Game over, {player1.name} wins!')
elif player2.score > player1.score:
    print(f'Game over, {player2.name} wins!')
else:
    print('Game over, nobody won :-(')
