# ZeroDivisionError : second arg of division is zero
# ValueError : receive arg that has right type but inappropriate value

# TEST CASES
# xx - 3/4 > 75%
# xx - 1/4 > 25%
# xx - 4/4 > F
# xx - 0/4 > E

# - 4/0 > ZeroDivisionError
# - three/four > ValueError
# - 1.5/3 > ValueError
# - 5/4 > reprompt user

def main():
    gauge = get_input()
    if gauge == 0.75:
        print("75%")
    elif gauge >= 0.50 and gauge <= 0.74:
        print("50%")
    elif gauge >= 0.25 and gauge <= 0.49:
        print("25%")
    elif gauge >= 0.76 and gauge <= 1.00:
        print("F")
    elif gauge >= 0 and gauge <= 0.24:
        print("E")

def get_input():
    while True:
        try:
            text = input("Fraction: ")
            nums = text.split('/')
            firstNum = int(nums[0])
            secondNum = int(nums[1])

            result = firstNum / secondNum

            if firstNum > secondNum:
                text = input("Fraction: ")

            return result

        except ValueError:
            text = input("Fraction: ")
        except ZeroDivisionError:
            text = input("Fraction: ")
        else:
            return result

main()