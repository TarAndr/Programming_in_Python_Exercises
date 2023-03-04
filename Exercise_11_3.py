# Lists in Python

nums = [int(i) for i in input('Input a numbers ').split()]

sums = []
n = len(nums)
for i in range(n):
    sums.append(nums[i - 1] + nums[i - n + 1])

print(nums)
print(sums)
