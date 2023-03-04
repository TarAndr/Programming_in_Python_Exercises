# Date and Time in Python

from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

dt1 = datetime.now()
print(dt1)

dt2 = dt1.strftime('%d %B %Y - %A')
print(dt2)

