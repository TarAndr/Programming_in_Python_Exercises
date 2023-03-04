# Tuples in Python

names1 = ('Andrey', 'Luba', 'Giorgi', 'Andrey', 'Vaso', 'Mari')
print('Tuple1 =', names1)

names2 = 'Andrey', 'Vaso', 'Nino', 'Andrey', 'Luba', 'Giorgi'
print('Tuple2 =', names2)

names3 = tuple(['Andrey', 'Vaso', 'Nino', 'Andrey', 'Luba', 'Giorgi', 'Vaso', 'Mari'])
print('Tuple3 =', names3)

for i in names3:
    print(i, end = ', ')

def getuser(name, age = 38):
    id = 123
    return id, name, age

print()
user1 = getuser(input('Input your name '))
print(user1)

for i in user1:
    print(i, end = ' ')
