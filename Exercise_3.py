# Logical operators in Python

a = 3
b = 5

# ==
c = a == b
print(c)

# !=
c = a != b
print(c)

# and
c = a > 2 and b < 7
print(c)

# or
c = a > 5 or b < 7
print(c)

# not
c = not a > 5
print(c)

if a < 7:
    print(True)
elif a > 7:
    print(False)
else:
    print("a = 7")
