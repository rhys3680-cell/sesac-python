class Box:
    def __init__(self, width, length, height):
        self.__width = width
        self.__length = length
        self.__height = height

    def setWidth(self, width):
        self.__width = width

    def getWidth(self):
        return self.__width

    def setLength(self, length):
        self.__length = length

    def getLength(self):
        return self.__length

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def getVolume(self):
        return self.__width * self.__length * self.__height
