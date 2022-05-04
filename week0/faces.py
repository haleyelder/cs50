# TEST CASES
# - Hello :) > Hello 🙂
# - Goodbye :( > Goodbye 🙁
# - Hello :) Goodbye :( > Hello 🙂 Goodbye 🙁

#ask for input
text = input()
text = text.replace(":)","🙂")
text = text.replace(":(", "🙁")
print(text)