# Functions in Python

def modif_list(items):
    for i in range(len(items) - 1, -1, -1):
        if items[i] % 2:
            items.remove(items[i])
        else:
            items[i] //= 2

nums = [int(i) for i in input('input numbers ').split()]

print(nums)

modif_list(nums)

print(nums)
