# Dictionaries in Python

lst1 = [i for i in range(2, 15, 3)]
print(lst1)

lst2 = [i for i in range(4, 25, 5)]
print(lst2)

dct = dict(zip(lst1, lst2))
print(dct)
