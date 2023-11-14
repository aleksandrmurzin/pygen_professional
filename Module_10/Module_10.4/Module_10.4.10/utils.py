# INPUT DATA:
class Fibonacci:
    def __init__(self) -> None:
        self.counter = 1
        self.prev_prev = 1
        self.prev = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= 2:
            self.counter += 1
            return 1
        curr = self.prev_prev + self.prev
        self.prev_prev = self.prev
        self.prev = curr

        return curr


# TEST_1:
fibonacci = Fibonacci()

print(next(fibonacci))

# TEST_2:
fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

# TEST_3:
fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

# TEST_4:
fibonacci = Fibonacci()

for _ in range(50):
    print(next(fibonacci))

# TEST_5:
fibonacci = Fibonacci()

for _ in range(100):
    next(fibonacci)

print(next(fibonacci))

# TEST_6:
fibonacci = Fibonacci()

for _ in range(76):
    next(fibonacci)

next(fibonacci)
next(fibonacci)
next(fibonacci)
next(fibonacci)

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

