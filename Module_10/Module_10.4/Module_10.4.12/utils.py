# INPUT DATA:
class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.iterator = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.iterator)
        return key, self.data[key]



# TEST_1:
pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)

# TEST_2:
data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

pairs = DictItemsIterator(data)

print(*pairs)

# TEST_3:
data = {'Arthur': 100, 'Timur': 100, 'Dima': 100,
        'Anri': 101, 'Roma': 99, 'German': 98}

pairs = DictItemsIterator(data)

print(list(pairs))

# TEST_4:
data = {'Arthur': [100, 5], 'Timur': [100, 6], 'Dima': [100, 7, 8],
        'Anri': [100, 101], 'Roma': [99]}

pairs = DictItemsIterator(data)

print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')

# TEST_5:
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

pairs = DictItemsIterator(data)

print(tuple(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')

