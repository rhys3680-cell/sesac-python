n = int(input("정수를 입력하시오: "))


def isOdd(n):
    return "입력된 정수는 짝수입니다." if n % 2 == 0 else "입력된 정수는 홀수입니다."


print(isOdd(n))
