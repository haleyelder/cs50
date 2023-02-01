# TESTS/FLOW
# - 25, 10, 5 allowed
# - calc how much is owed to reach 50
# - reprompt for only positive integers

print("Amount due: 50")

# #starting amount
changeOwed = 50


while changeOwed > 0:
    coins = int(input("Insert coins: "))

    #reprompt for positive integer
    if coins < 0:
        print("Amount due: 50")

    # valid inputs, subtract coins entered from total change (50)
    if coins == 25 or coins == 10 or coins == 5:
        changeOwed -= coins
        # if change goes below 0, break loop, print coins
        if changeOwed <= 0:
            break
            print(0)
        print("Change owed: " + str(changeOwed))
    else:
        print(50)

#return absolute value returned
print("Change owed: " + str(abs(changeOwed)))
