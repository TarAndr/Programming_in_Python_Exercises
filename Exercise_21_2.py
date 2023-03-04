# Classes in Python

from Exercise_21_2_mod import Person, Empl

pers = Person()
pers.show_info()
pers.name = 'Andrey'
pers.show_info()

empl = Empl(pers.name, 9999)
empl.show_info()
