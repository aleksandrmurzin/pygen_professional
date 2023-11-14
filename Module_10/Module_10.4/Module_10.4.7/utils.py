# INPUT DATA:
class Repeater:
    def __init__(self, obj):
        self.obj = obj


    def __next__(self):
        return self.obj

    def __iter__(self):
        return self

# TEST_1:
bee = Repeater('bee')

print(next(bee))

# TEST_2:
geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))

# TEST_3:
repeater = Repeater(1234)

for _ in range(100):
    print(next(repeater))

# TEST_4:
repeater = Repeater((1, 2, 3, 4))

for _ in range(55):
    print(next(repeater))

repeater = Repeater(['bee', 'geek'])

for _ in range(22):
    print(next(repeater))

