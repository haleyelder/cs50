# REFACTOR\

def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    newText = ""

    for i in range(len(word)):
        if word[i] not in vowels:
            newText += word[i]
    word = newText
    return word

if __name__ == "__main__":
    main()
