# Classes in Python

class Rectangle:
    def __init__(self, width, length):
        self.__width = int(width)
        self.__length = int(length)
    def p(self):
        return (self.__width + self.__length) * 2
    def s(self):
        return self.__width * self.__length

a = input('Input rectangle width ')
b = input('Input rectangle length ')

rect1 = Rectangle(a, b)

print('\tP =', rect1.p(), '\tS =', rect1.s())
