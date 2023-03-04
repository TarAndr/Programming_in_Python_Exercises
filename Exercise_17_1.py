# Modules in Python

import random

for i in range(22):
    print(random.random())

print()

for i in range(22):
    print(random.random() * 100)

print()

for i in range(22):
    print(random.randint(1, 99))

print()

for i in range(22):
    print(random.randrange(111, 333, 3))

print()

nums = [i for i in range(22)]

for i in nums:
    print(i, end = ' ')

random.shuffle(nums)

print('\n')

for i in nums:
    print(i, end = ' ')

print('\n')

print(random.choice(nums))
