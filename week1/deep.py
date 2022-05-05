# TEST CASES
# - 42 (str) >> Yes
# - forty two >> Yes
# - forty-two >> Yes
# - FoRTy TWO >> Yes
# - 50 >> No

text = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?" ))
#convert to lower case, remove hyphen, no space either side
answer = text.replace("-"," ").lower().strip()

if answer == "42":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")