# Cycles in Python
# while

while True:
    a = int(input('Input a number '))
    if a < 20:
        continue
    if a > 40:
        break
    print(a * a * a * a * a)
print('The end')
