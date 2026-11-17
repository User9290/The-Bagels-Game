# The Bagels Game
The Bagels Game, number guessing game, written completely in Python 3.15.2. This project is inspired by Al Sweigart's book "Big Book Of Small Python Projects", but I will improve this book idea.

So, I am new to GitHub, and I am here just to learn and have some fun. I am also not good at Python, I just learn, so, if you have any issues, recomendations, or questions, go to Github and share them, please.

# What is even this
So, The Bagels Game is fun, but a rather unknown (Where I live, no one knows it) number guessing game. It involves randomly guessing numbers and relying on the hints you get.
Computer thinks about a 3-digit number (If you want a menu or something to change number of digits, let me know, i will do my best to add it in future.) 
You guess a number, and you get one or two out of three clues:
- Pico,
- Fermi,
- or Bagels.

- Pico means that one digit in your number is correct, but is in the wrong position,
- Fermi means that one digit in your number is correct, and is in the right position,
- and Bagels means that no digit is correct in your number.

You can actually get 2 clues in one guess! Giving 3 clues would be too easy for you.
Clues are NOT sorted in order of digits, but alphabetically. So, Pico is always after Fermi. For example, if secret number is 123, and you will guess 253, clue will be Fermi Pico, not Pico Fermi.
You have 10 tries to get it right. If you want me to make a menu to change this and more, let me know on GitHub.

# How to launch this
Just launch the Game.py file.

# And what in the future?
You can check ROADMAP.md file to see what's next coming to this game.


Good Luck!
And have a nice day!

User9290

TIP: If you want, you can create a virtual environment with py -m venv venv, then activate it with venv\Scripts\Activate.