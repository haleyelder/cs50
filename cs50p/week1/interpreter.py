# FLOW
# x >> integer
# y >> +, -, *, or /
# z >> integer


def main():
    text = input("Expression: ")

    x, y, z = text.split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        print(add(x, z))
    elif y == "-":
        print(sub(x,z))
    elif y == "*":
        print(mult(x,z))
    elif y == "/":
        print(div(x,z))


def add(x, z):
    return x + z
def sub(x,z):
    return x - z
def mult(x,z):
    return round(x * z, 2)
def div(x,z):
    return round(x / z, 2)


main()
