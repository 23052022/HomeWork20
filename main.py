class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def add_1(self):
        if self.value <= self.end:
            self.value += 1
            return self.value

    def __str__(self):
        return f"{self.value}"

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value


x = Counter(1, 5)
x2 = Counter(1, 6)
print(x == x2)
x.add_1()
x2.add_1()
print(x)
print(x == x2)
