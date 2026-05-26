import random


def quiz():
    number = random.randint(1, 100)
    try_count = 0
    print(number)
    while True:
        n = int(input("1부터 100 사이의 숫자를 맞추시오"))
        try_count += 1
        if number < n:
            print("높음")
        elif number > n:
            print("낮음")
        elif try_count > 7:
            print("입력 횟수를 초과했습니다. 프로그램을 종료합니다.")
            return
        elif n == number:
            print(f"축하합니다. 시도 횟수 = {try_count}")
            return


quiz()
