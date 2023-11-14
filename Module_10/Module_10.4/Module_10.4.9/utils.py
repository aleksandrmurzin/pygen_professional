# INPUT DATA:
class Square:

    def __init__(self, n):
        self.n = n
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            self.n -= 1
            self.number += 1
            return (self.number - 1) ** 2
        raise StopIteration


# TEST_1:
squares = Square(2)

print(next(squares))
print(next(squares))

# TEST_2:
squares = Square(10)

print(list(squares))

# TEST_3:
squares = Square(1)

print(list(squares))

# TEST_4:
squares = Square(5)

next(squares)
next(squares)
next(squares)
next(squares)
next(squares)

try:
    next(squares)
except StopIteration:
    print('Error')

# TEST_5:
squares = Square(9)

print(*squares)

# TEST_6:
squares = Square(2)

try:
    print(next(squares))
    print(next(squares))
    print(next(squares))
except:
    print('Error')

