1. `__eq__` 매직 메서드 (test16)

    ```python
    class Car:
        def __init__(self, color="white", speed=0):
            self.__color = color
            self.__speed = speed

        def __eq__(self, other):
            return (self.__color == other.__color) and (self.__speed == other.__speed)
    ```

    - 서로 다른 주소값이어도 `==`가 `True`인 이유는 `a.__eq__(b)`로 동작하기 때문
    - `__eq__`는 빌트인 `object` 클래스에서 기본 상속되며, 재정의 시 동등성 기준을 직접 정함

2. property / setter 검증 (test17)

    ```python
    class Person:
        def __init__(self, name, age=0):
            self.name = name
            self.age = age

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, new_age):
            if not isinstance(new_age, int) or isinstance(new_age, bool):
                raise ValueError(f"age must be int, got {type(new_age).__name__}")
            if new_age < 0:
                raise ValueError(f"age must be non-negative, got {new_age}")
            self.__age = new_age
    ```

    - `@property` / `@<속성>.setter`로 읽기·쓰기를 메서드로 감싸 검증 로직 삽입
    - `__eq__`와 `__hash__`를 함께 정의해야 set/dict 키로 안전하게 사용 가능
    - `__str__`(사람용) vs `__repr__`(개발자용, 리스트/딕셔너리 출력)

3. 위임 패턴으로 리스트 인터페이스 구현 (test18)

    ```python
    class MyList:
        def __init__(self, data=None):
            self.__data = list(data) if data is not None else []

        def append(self, item):
            self.__data.append(item)

        def __getitem__(self, index):
            result = self.__data[index]
            return MyList(result) if isinstance(index, slice) else result

        def __len__(self):
            return len(self.__data)

        def __add__(self, other):
            if not isinstance(other, MyList):
                return NotImplemented
            return MyList(self.__data + other.__data)
    ```

    - 내부에 실제 `list`를 두고(`self.__data`), 메서드 호출을 그 리스트로 위임(delegation)
    - 매직 메서드(`__getitem__`, `__len__`, `__contains__`, `__iter__`, `__add__`, `__iadd__` ...)를 구현하면 인덱싱·슬라이싱·`in`·`for`·`+` 연산을 내장 리스트처럼 사용 가능
    - 슬라이싱 결과도 `MyList` 타입을 유지하도록 처리

4. 로또 당첨 순위 계산 (test19)

    ```python
    def solution(lottos: list, win_nums: list) -> list:
        rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}  # 맞힌 개수 -> 순위
        zero_count = lottos.count(0)
        match_count = len(set(lottos) & set(win_nums) - {0})

        max_match = match_count + zero_count  # 0이 전부 당첨이라 가정 (최고)
        min_match = match_count               # 0이 전부 꽝이라 가정 (최저)

        return [rank.get(max_match, 6), rank.get(min_match, 6)]
    ```

    - 가려진 번호(`0`)는 전부 맞았을 때 최고 순위, 전부 틀렸을 때 최저 순위로 계산
    - `set` 교집합으로 맞힌 개수를 구하고, `dict.get(key, 6)`으로 6개 미만이면 낙첨(6위) 처리
