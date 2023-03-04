# Date and Time in Python

from datetime import datetime

dt1 = datetime.strptime('27/02/2023', '%d/%m/%Y')
print(dt1)

dt1 = datetime.strptime('27/02/2023 13:57', '%d/%m/%Y %H:%M')
print(dt1)

dt1 = datetime.strptime('02-27-2023 13.57', '%m-%d-%Y %H.%M')
print(dt1)
