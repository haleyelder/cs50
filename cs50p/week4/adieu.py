# "Adieu, adieu, to {name, name, name}"
# , and {name}
# input at least one name

# TESTS
# - 1 name, no and
# "Adieu, adieu, to Liesl"
# - 2 names, no comma and and
# Adieu, adieu, to Liesl and Friedrich
# - 3+ names, comma and and
# Adieu, adieu, to Liesl, Friedrich, and Louisa

import sys
import inflect
p = inflect.engine()

namesList = []

while True:
    try:
        names = input("Name: ").title()
        if len(names) < 1:
            sys.exit()

        namesList.append(names)
        output = p.join(namesList)

    except EOFError:
        print('\n')
        print("Adieu, adieu, to " + output)
        break
    else:
        continue