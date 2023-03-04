# Logical operators in Python

a = input("a = ")
b = input("b = ")

if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a = b")

# swap a and b
a, b = b, a
print("a = ", a, ", b = ", b)
