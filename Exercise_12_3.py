# Lists in Python

nums = [int(i) for i in input('Input list of numbers ').split()]
x = int(input('Input the one number '))

indexes = []

for i in range(len(nums)):
    if nums[i] == x:
        indexes.append(i)

if len(indexes):
    print('Indexes of number', x, 'in', nums, '=', indexes)
else:
    print('The number', x, 'not in list', nums)
