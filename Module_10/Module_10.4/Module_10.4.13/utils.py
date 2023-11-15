# INPUT DATA:
class CardDeck:
    def __init__(self):
        from itertools import product

        self.curr_card_rank = 0
        self.ranks = iter((2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"))
        self.suits = iter(("пик", "треф", "бубен", "червей"))
        self.cards = product(self.suits, self.ranks)

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_card_rank += 1
        if self.curr_card_rank > 52:
            raise StopIteration

        suit, rank = next(self.cards)
        return f"{rank} {suit}"


# TEST_1:
cards = CardDeck()

print(next(cards))
print(next(cards))

# TEST_2:
cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])

# TEST_3:
cards = list(CardDeck())

print(cards)

# TEST_4:
cards1 = list(CardDeck())
cards2 = tuple(CardDeck())
cards3 = list(CardDeck())

print(cards1)
print(cards2)
print(cards3)

# TEST_5:
cards = list(CardDeck())

try:
    next(cards)
except:
    print('Error')

