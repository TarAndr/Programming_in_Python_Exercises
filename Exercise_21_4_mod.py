# Classes in Python

class Person:
    """Class for person"""
    def __init__(self, name = 'Andro', age = 38):
        self.__name = name      # Privat atribute
        self.__age = age
    def __del__(self):
        print(self.__name, 'was deleted')
    def show_info(self):
        print('\tName', self.__name, '\tAge', self.__age)
    @property       # Getter
    def name(self):
        return self.__name
    @name.setter    # Setter
    def name(self, name):
        self.__name = name
    @property       # Getter
    def age(self):
        return self.__age
    @age.setter    # Setter
    def age(self, age):
        self.__age = age

class Employee (Person):
    def __init__(self, name, age, sal):
        Person.__init__(self, name, age)
        self.__sal = sal
    @property
    def sal(self):
        return self.__sal
    @sal.setter
    def sal(self, sal):
        self.__sal = sal
    def show_info(self):
        Person.show_info(self)
        print('\tSalary', self.__sal)
