# REFACTOR

def main():
    text = input("Greeting: ")
    greeting = value(text)
    print(greeting)

def value(greeting):
    # accept str as input, return int values
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

