# TEST CASES
# - 1 > 90000000000000000
# - 14 > 1260000000000000000
# - 50 > 4500000000000000000check50 cs50/problems/2022/python/einstein
# E = mc2

# E (joules)
# m = input (kg)
# c squared = 300000000 ** 2

m = input("m: ")
E = int(m) * (300000000 ** 2)
print(f"E: {E}")