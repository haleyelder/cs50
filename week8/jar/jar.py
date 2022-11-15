class Jar:
    # capacity non negative, otherwise valueerror
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    # returns str with n cookies, returns emojis
    def __str__(self):
        return "🍪" * self.size

    # add cookies to jar, if goes over capacity, value error
    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError
        self._size += n
        # return capacity

    # remove cookies from jar, if remove is over totaly, value error
    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n

    # max capacity of jar (total after calculation)
    @property
    def capacity(self):
        return self._capacity

    # current number of cookies in jar
    @property
    def size(self):
        return self._size

# manual testing
def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    print(jar.capacity)
    print(jar.size)

if __name__ == "__main__":
    main()