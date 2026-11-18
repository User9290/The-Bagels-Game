"""The Bagels Game, author: User9290, inspired by Al Sweigart's book "Big Book Of Small Python Projects."
A logic deduction game, where you have to guess the number based on clues."""

import random

NUM_DIGITS = 3 #I will try to make this number changable from level of UI.
MAX_GUESSES = 10 #And this number too.

def main():
    print("""The Bagels Game, logic deduction game.
Author: User9290, inspired by Al Sweigart's book "Big Book Of Small Python Projects"

I think about {}-digit number, and in this number no digit repeats.
Try to guess it. After each guess, I will give you clues. Here are the list of every clue you get.
When I say:      That means:
    Pico         One digit is correct, but is in the wrong position.
    Fermi        One digit is correct, and is in the right position.
    Bagels       No digit is correct.
    
For example, if the secret number is 248, and you will guess 843,
clue will be Fermi Pico.""".format(NUM_DIGITS))

    while True: #Main loop.
        #This variable stores the number, that player has to guess:
        