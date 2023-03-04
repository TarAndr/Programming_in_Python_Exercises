# Lists in Python

nums = [int(i) for i in input('Input list of numbers ').split()]

print(nums)

i_min = nums.index(min(nums))
i_max = nums.index(max(nums))

nums[i_min], nums[i_max] = nums[i_max], nums[i_min]

print(nums)
