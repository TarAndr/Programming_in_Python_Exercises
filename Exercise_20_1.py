# Classes in Python

class Person:
    name = 'Andro'
    def show_info(self):
        print('My neme is', self.name)


pers1 = Person()
pers1.show_info()

pers2 = Person()
pers2.name = 'Luba'
pers2.show_info()

pers3 = Person()
pers3.name = input('Input name of object ')
pers3.show_info()
