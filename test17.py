class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError(f"name must be str , got {type(new_name).__name__}")
        self.__name = new_name

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or isinstance(new_age, bool):
            raise ValueError(f"age must be int, got {type(new_age).__name__}")

        if new_age < 0:
            raise ValueError(f"age must be non-negative, got {new_age}")

        self.__age = new_age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))

    def __str__(self):
        return f"name={self.name}, age={self.age}"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"


han = Person("han", 21)
kim = Person("kim", 24)
han2 = Person("han", 21)

# 속성 접근
print(han.name, han.age)
print(kim.name, kim.age)

# __eq__
print(han == kim)   # False
print(han == han2)  # True
print(han == "han") # False (다른 타입은 NotImplemented → False)

# __hash__ (set/dict 키로 사용 가능)
people = {han, kim, han2}
print(len(people))  # 2 (han과 han2는 동등하므로 하나로 취급)

# __str__ (print 시 사용)
print(han)          # name=han, age=21

# __repr__ (리스트/딕셔너리 안에서 사용)
print([han, kim])   # [Person(name='han', age=21), Person(name='kim', age=24)]

# setter 검증
try:
    han.age = -1
except ValueError as e:
    print(e)        # age must be non-negative, got -1

try:
    han.name = 123
except ValueError as e:
    print(e)        # name must be str , got int
