# - must input pos int (reprompt)
# - if guess less than int, "Too small!" (reprompt)
# - if larger, "Too large!" (reprompt)
# - "Just right!"

import random

while True:
    level = input("Level: ")

    # LEVEL: check string and < 0
    if not int(level.isdecimal()) or int(level) < 0:
        level = input("Level: ")

    guess = input("Guess: ")

    # GUESS: check string and < 0
    if not int(guess.isdecimal()) or int(guess) < 0:
        guess = input("Guess: ")

    number = random.randint(1, int(level))

    if int(guess) > number:
        print("Too large!")
    elif int(guess) < number:
        print("Too small!")
    else:
        print("Just right!")
        break