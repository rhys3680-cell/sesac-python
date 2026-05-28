a = 12


def my_func(a):
    a += 1
    return a


a = my_func(a)

assert a == 13, "a의 값은 변한다."

print(f"검증 성공 a의 값은 {a}입니다.")
