class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age
