# Cycles in Python
# for

n = abs(int(input('Calculate factorial\n\tInput \"n\" = ')))
i = 1
f = 1

for i in range(1, n + 1):
    f *= i

print('Factorial', n, '=', f)
