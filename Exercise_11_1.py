# Lists in Python

import copy

items = [5, 16, 3, 19, 8, 11, 25, 13]

print(min(items))

print(max(items))

items2 = copy.deepcopy(items)

items2.append(22)

items3 = items2[2 : 7 : 2]
items3.append(11)

print(items)
print(items2)
print(items3)
