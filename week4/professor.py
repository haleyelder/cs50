import sys
import random

def main():
    num = get_level()

    errors = 1
    score = 0

    for i in range(10):
        x = generate_integer(num)
        for j in range(1):
            y = generate_integer(num)

            answer = x + y
            equation = input(f"{x} + {y} = ")

            if int(equation) == answer:
                score += 1

            while int(equation) != answer:
                errors += 1
                print("EEE")
                equation = input(f"{x} + {y} = ")
                if errors >= 3:
                    print(answer)
                    sys.exit("Score: " + str(score))

    print("Score: " + str(score))

# prompt for level and reprompt if needed
def get_level():
    levelChoice = input("Level: ")

    if levelChoice.isalpha() or int(levelChoice) <= 0 or int(levelChoice) > 3:
        input("Level: ")
    else:
        levelChoice = int(levelChoice)
        for i in [1,2,3]:
            if levelChoice == i:
                return levelChoice

# generate int from level choice
def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
    except:
        raise ValueError

if __name__ == "__main__":
    main()