# Lists in Python

nums = [int(i) for i in input('Input list of numbers ').split()]

sim = 1
for i in range(len(nums) // 2):
    if nums[i] != nums[len(nums) - i -1]:
        sim = 0
        break

if sim:
    print('Inputed list is simetrial')
else:
    print('Inputed list is not simetrial')
