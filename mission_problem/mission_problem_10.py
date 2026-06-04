str = "강아지의 이름을 입력하시오(종료시에는 엔터키)"
dogNameList = list()

while True:
    dogName = input(str)
    dogNameList.append(dogName)
    if dogName == "":
        dogNameList.pop()
        print(dogNameList)
        break
