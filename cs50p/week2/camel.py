# TESTS
# convert input from camel to snake case
# name > name
# firstName > first_name
# preferrdFirstName > preferred_first_name

text = input("camelCase: ")

# loop word for letters
for n in text:
    # check for uppercase and replace with _letter
    if n.isupper():
        newText = "_" + n.lower()
        # replace letter with updated _letter
        n = newText
    #print!
    print(n, end="")

