# Cycles in Python
# while

n = abs(int(input('Calculate factorial\n\tInput \"n\" = ')))
i = 1
f = 1

while i <= n:
    f *= i
    i += 1

print('Factorial', n, '=', f)
