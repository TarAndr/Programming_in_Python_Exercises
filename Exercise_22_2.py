# Classes in Python

class Rectangle:
    def __init__(self, width, length):
        self.__width = int(width)
        self.__length = int(length)
        self.__p = (self.__width + self.__length) * 2
        self.__s = self.__width * self.__length
    @property
    def p(self):
        return self.__p
    @property
    def s(self):
        return self.__s

a = input('Input rectangle width ')
b = input('Input rectangle length ')

rect1 = Rectangle(a, b)

print('\tP =', rect1.p, '\tS =', rect1.s)
