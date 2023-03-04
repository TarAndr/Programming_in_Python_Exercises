# Classes in Python

class Person:
    def __init__(self, name_ = 'Andro'):
        self.name = name_
    def __del__(self):
        print(self.name, 'was deleted')
    def show_info(self):
        print('My name is', self.name)

class Empl:
    """Class for employes"""
    cnt = 0
    def __init__(self, name_, sal_):
        self.name = name_
        self.sal = sal_
    def __del__(self):
        print(self.name, 'was deleted')
    def show_info(self):
        print('\tName', self.name, '\tSalary', self.sal)
