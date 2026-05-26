class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def __eq__(self, carB):
        return self.color == carB.color

    def __str__(self):
        return "color = %s, speed = %d" % (self.color, self.speed)


Car1 = Car("black", 0)
Car2 = Car("red", 120)
Car3 = Car("yellow", 30)
Car4 = Car("green", 0)
Car5 = Car("blue")
Car6 = Car("yellow")

print(Car1, Car2, Car3, Car4, Car5, Car6)


class SuperCar(Car):
    def __init__(self, color, speed=0, bTurbo=True):
        super().__init__(color, speed)
        self.bTurbo = bTurbo

    def setTurbo(self, bTurbo=True):
        self.bTurbo = bTurbo

    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()

    def __str__(self):
        if self.bTurbo:
            return "[%s] [speed = %d] 터보모드" % (self.color, self.speed)
        else:
            return "[%s] [speed = %d] 일반모드" % (self.color, self.speed)
