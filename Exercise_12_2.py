# Lists in Python

n = int(input('Input the \"n\" '))

nums = []

for i in range(n + 1):
    for j in range(i):
        nums.append(i)

for i in range(n):
    print(nums[i], end = ' ')
