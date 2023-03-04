# Dictionaries in Python

users = {}  #empty dict
users = dict()  #empty dict from function
users1 = {1: 'Andrey', 2: 'Luba', 3: 'Vaso'}
users2 = {'A': 'Andrey', 2: 'Luba', 'B': 'Vova', 3: 'Vaso'}

users_list = [
        [1, 'Andrey'],
        [2, 'Luba'],
        [3, 'Vova'], 
        [4, 'Vaso']
    ]

users = dict(users_list)    #dict from list

print(users1)
print(users2)
print(users)

users.clear()
print(users)

users_tuple = (
        (3, 'Andrey'),
        (1, 'Luba'),
        (0, 'Vova'), 
        (2, 'Vaso')
    )

users = dict(users_tuple)    #dict from tuple
print(users)

users[4] = 'Dato'

for i in users:
    print(i, users[i])

id = int(input('Input the ID for view user '))

if id in users:
    print('User with ID =', id, 'is', users[id])
else:
    print('User with ID =', id, 'is not exist')

print(users.get(id, 'User is not exist'))

id = int(input('Input the ID for delete user '))

if id in users:
    del users[id]
    print('User with ID =', id, 'is deleted')
else:
    print('User with ID =', id, 'is not exist')

id = int(input('Input the ID for delete user '))

deleted = users.pop(id, 'not exist')    

print('Deleted user is', deleted)
print(users)

users = users1.copy()
print(users1)
print(users)

users.update(users2)
print(users)

print(users.keys())
print(users.values())
print(users.items())

for key in users.keys():
    print(key, end = ' ')

print()

for val in users.values():
    print(val, end = ' ')

print()

for key, val in users.items():
    print(key, val)
