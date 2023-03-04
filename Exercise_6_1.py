# Calculate square of shape

shape = int(input('Input type of shape:\n\t1 - triangle\n\t2 - square\n\t3 - circle\n'))

if shape == 1:
    a = int(input('\tinput \"a\" = '))
    b = int(input('\tinput \"b\" = '))
    c = int(input('\tinput \"c\" = '))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('Square is', s)
elif shape == 2:
    a = int(input('\tinput \"a\" = '))
    b = int(input('\tinput \"b\" = '))
    s = a * b
    print('Square is', s)
elif shape == 3:
    r = int(input('\tinput \"r\" = '))
    s = 3.14159265 * r * r
    print('Square is', s)
else:
    print('Square is not defined')
