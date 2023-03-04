# Lists in Python

nums = [int(i) for i in input('Input list of numbers ').split()]

print(nums)

temp = nums[0]
for i in range(len(nums) - 1):
    nums[i] = nums[i - len(nums) + 1]

nums[len(nums) - 1] = temp

print(nums)
