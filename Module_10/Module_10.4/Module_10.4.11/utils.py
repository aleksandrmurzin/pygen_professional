# INPUT DATA:
from functools import lru_cache

class PowerOf:
    def __init__(self, number):
        self.number = number
        self.power = 0

    def __iter__(self):
        return self

    def __next__(self):
        @lru_cache
        def powerof(number, power):
            if power == 0:
                return 1
            return number * powerof(number, power - 1)

        answer = powerof(self.number, self.power)
        self.power += 1
        return answer


# # TEST_1:
# power_of_two = PowerOf(2)

# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))

# # TEST_2:
# power_of_two = PowerOf(1)

# for _ in range(55):
#     print(next(power_of_two))

# # TEST_3:
# power_of_two = PowerOf(3)

# for _ in range(10):
#     print(next(power_of_two))

# # TEST_4:
# power_of_two = PowerOf(11)

# for _ in range(11):
#     print(next(power_of_two))

# TEST_5:
power_of_two = PowerOf(3332.7)

for _ in range(99):
    print(next(power_of_two))

# print(next(power_of_two))

