# Classes in Python

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

print(Empl.__doc__)
print(Empl.__name__)
print(Empl.__module__)
print(Empl.__dict__)
