# Classes in Python

class Person:
    name = ''
    def __init__(self, name_ = 'Andro'):
        self.name = name_
    def show_info(self):
        print('My neme is', self.name)


pers1 = Person()
pers1.show_info()
del pers1

pers2 = Person('Luba')
pers2.show_info()
del pers2

pers3 = Person()
pers3.name = input('Input name of object ')
pers3.show_info()
del pers3
