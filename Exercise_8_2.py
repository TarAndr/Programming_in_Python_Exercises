# Cycles in Python
# while

a = int(input('Input number \"a\" = '))
b = int(input('Input number \"b\" = '))
d = 1

while d % a or d % b:
    d += 1

print('The \"d\" =', d)
