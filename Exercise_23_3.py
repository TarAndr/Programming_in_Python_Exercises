# Date and Time in Python

from datetime import datetime

dt1 = datetime(2023, 9, 27)
print(dt1)

dt1 = datetime(2023, 9, 27, 15, 16, 17, 18)
print(dt1)

dt1 = datetime.now()
print(dt1)

print(dt1.year)
print(dt1.month)
print(dt1.day)
print(dt1.hour)
print(dt1.minute)
print(dt1.second)
