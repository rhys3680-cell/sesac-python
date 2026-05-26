import math


class Circle:
    def __init__(self, radius=1.0):
        self.__radius = radius

    def setRadius(self, r):
        self.__radius = r

    def getRadius(self):
        return self.__radius

    def calcArea(self):
        return math.pi * self.__radius**2

    def calcCircum(self):
        return 2.0 * math.pi * self.__radius
