# TEST CASES
# - list out list alphabetically
# - number count of items to left
# - all uppercase

groceryList = []
tally = {}

while True:
    try:
        item = input("")
        item = item.upper()

        groceryList.append(item)
        groceryList.sort()

    except EOFError:
        for item in groceryList:
            if item in tally:
                tally[item] += 1
            else:
                tally[item] = 1
        for x in tally:
            print(str(tally[x]) + " " + x)
        break
    else:
        continue