# Lists in Python

nums = [int(i) for i in input('Input a numbers ').split()]

sum = 0
for i in nums:
    sum += i

print(nums)
print('Sum of numbers =', sum)
