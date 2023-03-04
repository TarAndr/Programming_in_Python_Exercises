# Modules in Python

from decimal import Decimal

num = Decimal('0.0130')

sum = 0

for i in range(73):
    sum += num

print(sum)

num = Decimal('0.0137524')

print(num.quantize(Decimal('0.0000')))
