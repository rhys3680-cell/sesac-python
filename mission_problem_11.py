str1 = """
1. 친구 리스트 출력
2. 친구추가
3. 친구삭제
4. 이름변경
9. 종료
"""

str2 = "메뉴를 선택하시오:"

str3 = "이름을 입력하시오:"

str4 = "-----------------"

friendsList = list()

while True:
    print(str4)
    print(str1)
    menuNumber = input(str2)

    if menuNumber == "1":
        print(friendsList)
        print(str4)

    if menuNumber == "2":
        friendName = input(str3)
        friendsList.append(friendName)
        print(str4)

    if menuNumber == "3":
        friendName = input(str3)
        friendsList.remove(friendName)
        print(str4)

    if menuNumber == "4":
        friendName = input(str3)
        friendsList.remove(friendName)
        friendsList.append(friendName)
        print(str4)

    if menuNumber == "9":
        break
