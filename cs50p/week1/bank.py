# # TEST CASES
# "Hello" > $0
# "Hello, Newman" > $0
# How are you doing? > $20
# What's happening? > $100

# FLOW
# hello (first word in phrase as well) >> $0
# starts with "h" >> $20
# else >> $100

text = input("Greeting: ")
response = text.lower().strip()

if response.startswith("hello"):
    print("$0")
elif response.startswith("h"):
    print("$20")
else:
    print("$100")