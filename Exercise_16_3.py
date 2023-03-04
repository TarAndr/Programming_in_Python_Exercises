# Dictionaries in Python

def update_dict(dictionary, key, value):
    if key in dictionary:
        dictionary[key] += [value]
    elif key * 2 in dictionary:
        dictionary[key * 2] += [value]
    else:
        dictionary[key] = [value]

nums = {i : [(i + 7) * (18 - i)] for i in range(10, 30, 2)}

print(nums)

k = int(input('Input the key for update '))
v = int(input('Input the value for update '))

update_dict(nums, k, v)

for i, j in nums.items():
    print(i, j)
