# Classes in Python

from Exercise_21_1_mod import Person, Empl

pers = Person('Andrey')
pers.show_info()

empl = Empl(pers.get_name(), 9999)
empl.show_info()
