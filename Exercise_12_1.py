# Lists in Python

nums = [int(i) for i in input('Input a numbers ').split()]
nums2 = []

for i in nums:
    if nums.count(i) > 1 and nums2.count(i) == 0:
        nums2.append(i)

print(nums)
print(nums2)
