# INPUT DATA:
class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __next__(self):
        if self.times > 0:
            self.times -= 1
            return self.obj
        raise StopIteration

    def __iter__(self):
        return self


# TEST_1:
bee = BoundedRepeater('bee', 2)

print(next(bee))
print(next(bee))

# TEST_2:
geek = BoundedRepeater('geek', 3)

print(next(geek))
print(next(geek))
print(next(geek))

try:
    print(next(geek))
except StopIteration:
    print('Error')

# TEST_3:
repeater = BoundedRepeater(['bee', 'geek'], 10)

for _ in range(9):
    next(repeater)

print(next(repeater))

try:
    next(repeater)
except StopIteration:
    print('Error')

# TEST_4:
repeater = BoundedRepeater(9999, 1)

try:
    print(next(repeater))
    print(next(repeater))
except StopIteration:
    print('Error')

# TEST_5:
repeater = BoundedRepeater((1, 2, 3, 4), 15)

for _ in range(10):
    next(repeater)

next(repeater)
next(repeater)
next(repeater)
next(repeater)
next(repeater)

try:
    print(next(repeater))
except StopIteration:
    print('Error')

# TEST_6:
repeater = BoundedRepeater({'bee': 'geek'}, 55)

for elem in repeater:
    print(elem)

# TEST_7:
repeater = BoundedRepeater(1, 10)

print(list(repeater))

