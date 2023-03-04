# Lists in Python

nums1 = [1, 3, 5, 7, 9]

nums2 = list(nums1)

print(nums1[0])
print(nums1[2])
print(nums1[-1])

nums1[2] = 11
print(nums1[2])

print(nums1)
print(nums2)

nums1 = [0] * 7
print(nums1)

nums2 = list(range(2, 18, 3))
print(nums2)

items = ['One', 2, 3.14159265, True]
print(items)

for i in items:
    print(i)

items.append(False)
for i in items:
    print(i)

items.insert(3, 4)
print(items)

i = items.index(True)
poped = items.pop(i)
print(i, poped, items)

if False in items:
    items.remove(False)
print(items)

items.clear()
print(items)

nums2.reverse()
print(nums2)

nums2.sort()
print(nums2)
