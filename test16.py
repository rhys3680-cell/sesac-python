# Car라는 클래스(설계도)를 만듦
class Car:
    def __init__(self, color="white", speed=0):
        self.__color = color
        self.__speed = speed

    def get_color(self):
        return self.__color

    def get_speed(self):
        return self.__speed

    def __eq__(self, other):
        return (self.__color == other.__color) and (self.__speed == other.__speed)


# a, b라는 변수에 Car라는 클래스를 사용한 인스턴스를 만듦, speed=10
a = Car(speed=10)
b = Car(speed=10)

if a == b:
    print("same")

else:
    print("diff")

print(a)
print(b)

# same
# <__main__.Car object at 0x000002A63E25AE40>
# <__main__.Car object at 0x000002A63E29C190>

# 서로 다른 주소값이지만 == 연산 결과가 True인 이유는 내부적으로 a.__eq__(b)로 동작하기 때문
# __eq__는 어디에서 왔는가?
# 파이썬 빌트인 object 클래스의 기본적으로 상속
# def __eq__(self, value: object, /) -> bool: ...
# 자바는 기본적으로 encapsulation
# 파이썬은 개방적인 encapsulation
# object 클래스의 __eq__ 메서드를 향하려면 super()를 활용
