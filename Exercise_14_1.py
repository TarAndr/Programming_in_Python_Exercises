# Sets in Python

names1 = {'Andrey', 'Luba', 'Giorgi', 'Andrey', 'Vaso', 'Mari'}
print('Set 1 =', names1)

names2 = set(['Andrey', 'Vaso', 'Nino', 'Andrey', 'Luba', 'Giorgi'])
print('Set 2 =', names2)

names3 = set()
names3.add(input('Input your name '))
print('Set 3 =', names3)

if names3.issubset(names1):
    print('Set3 is subset of set1')

if names2.issuperset(names3):
    print('Set2 is superset of set3')

name = input('Input name for remove from set 1 ')
if name in names1:
    names1.remove(name)
    print('Name', name, 'was removed from set 1')
else:
    print('The name', name, 'not existing in set 1')

print('Set 1 =', names1)

name = input('Input name for remove from set 2 ')
names2.discard(name)
print('Set 2 =', names2)

print('Set1 & Set2', names1 & names2)

names3 = names1.intersection(names2)
print('Set 3 =', names3)

print('Set1 - Set2', names1 - names2)

names3 = names1.difference(names2)
print('Set 3 =', names3)

names3 = names1.union(names2)
print('Set 3 =', names3)

names2.clear()
print('Set 2 =', names2)

for i in names1:
    print(i, end = ' ')

names2 = names1.copy()
print('')
print('Set 1 =', names1)
print('Set 2 =', names2)

