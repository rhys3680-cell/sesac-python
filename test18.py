class MyList:
    def __init__(self, data=None):
        self.__data = list(data) if data is not None else []

    # 변경 (mutating) 메서드
    def append(self, item):
        self.__data.append(item)

    def extend(self, iterable):
        self.__data.extend(iterable)

    def insert(self, index, item):
        self.__data.insert(index, item)

    def pop(self, index=-1):
        return self.__data.pop(index)

    def remove(self, item):
        self.__data.remove(item)

    def clear(self):
        self.__data.clear()

    def reverse(self):
        self.__data.reverse()

    def sort(self, *, key=None, reverse=False):
        self.__data.sort(key=key, reverse=reverse)

    # 조회 (non-mutating) 메서드
    def index(self, item, *args):
        return self.__data.index(item, *args)

    def count(self, item):
        return self.__data.count(item)

    def copy(self):
        return MyList(self.__data)

    # 매직 메서드
    def __getitem__(self, index):
        result = self.__data[index]
        return MyList(result) if isinstance(index, slice) else result

    def __setitem__(self, index, value):
        self.__data[index] = value

    def __delitem__(self, index):
        del self.__data[index]

    def __len__(self):
        return len(self.__data)

    def __contains__(self, item):
        return item in self.__data

    def __iter__(self):
        return iter(self.__data)

    def __reversed__(self):
        return reversed(self.__data)

    def __add__(self, other):
        if not isinstance(other, MyList):
            return NotImplemented
        return MyList(self.__data + other.__data)

    def __iadd__(self, other):
        if isinstance(other, MyList):
            self.__data += other.__data
        else:
            self.__data += list(other)
        return self

    def __eq__(self, other):
        if not isinstance(other, MyList):
            return NotImplemented
        return self.__data == other.__data

    def __str__(self):
        return f"{self.__data}"

    def __repr__(self):
        return f"MyList({self.__data!r})"


mlst1 = MyList()
mlst1.append(10)
mlst1.extend([20, 30])
mlst1.insert(0, 5)
print(mlst1)              # [5, 10, 20, 30]
print(len(mlst1))         # 4
print(mlst1[0])           # 5
print(mlst1[1:3])         # [10, 20]  ← MyList 타입 유지

mlst2 = MyList([3, 4, 5])
mlst3 = mlst1 + mlst2
print(mlst3)              # [5, 10, 20, 30, 3, 4, 5]

mlst1 += [99, 100]
print(mlst1)              # [5, 10, 20, 30, 99, 100]

print(20 in mlst1)        # True
print(mlst1.count(20))    # 1
print(mlst1.index(30))    # 3

mlst1.sort(reverse=True)
print(mlst1)              # [100, 99, 30, 20, 10, 5]

for x in mlst1:
    print(x, end=" ")
print()