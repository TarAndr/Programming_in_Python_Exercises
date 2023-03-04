# Date and Time in Python

from datetime import timedelta, datetime

dt1 = timedelta(4, hours = 8, minutes = 53)
print(dt1)

dt2 = datetime.now()
print(dt2)
print(dt2 - dt1)
