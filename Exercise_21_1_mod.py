# Classes in Python

class Person:
    def __init__(self, name = 'Andro'):
        self.__name = name      # Privat atribute
    def __del__(self):
        print(self.__name, 'was deleted')
    def show_info(self):
        print('My name is', self.__name)
    def get_name(self):
        return self.__name

class Empl:
    """Class for employes"""
    cnt = 0
    def __init__(self, name, sal):
        self.__name = name      # Privat atribute
        self.__sal = sal      # Privat atribute
    def __del__(self):
        print(self.__name, 'was deleted')
    def show_info(self):
        print('\tName', self.__name, '\tSalary', self.__sal)
