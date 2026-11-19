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
        secretNum = getSecretNum()
        print("I mean the number.")
        print("You have {} tries to guess what number it is.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Running a loop until the player enters the correct number:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Attempt #{}: ".format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break #The number entered is correct, end the loop.
            if numGuesses > MAX_GUESSES:
                print("You've used all your tries.")
                print("The correct answer is: {}.".format(secretNum))

        #Ask the player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith("y"):
            break
    print("Thanks for playing!")

def getSecretNum():
    """Returns a number made up of as many random, unique digits as the value of NUM_DIGITS."""
    numbers = list('0123456789') #Make a list of digits from 0 to 9.
    random.shuffle(numbers) #Set them in a random order.

    #Add more digits to the secret number.
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string of Pico, Fermi, Bagels for a given guess
    or information about a win."""
    if guess == secretNum:
        return "You did it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #The correct number in a right place.
            clues.append("Fermi")
        elif guess[i] in secretNum:
            #The right number in the wrong place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels" #No correct digits.
    else:
        #Arrange the clues in alphabetical order,
        #so that their order wouldn't reveal too much information.
        clues.sort()
        #Combine all the hints into a single string.
        return " ".join(clues)


#If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()