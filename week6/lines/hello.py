def main():
    name = input("whats your name? ")
    print(hello(name))

def hello(to="world"): # test internal
    return f"hello, {to}"