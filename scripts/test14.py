while True:
    usernum = input("중복되지 않은 네 자리 숫자를 입력하시오~!!!")
    try:
        usernum = list(map(int, usernum))
    except:
        print("너 돌아이지?")
        continue
    if len(usernum) == 4:
        check = 0
        for num in usernum:
            if usernum.count(num) > 1:
                check = 1  # 중복된 숫자 발견
        if check == 1:
            continue
        else:
            break
    else:
        continue
print(usernum)
