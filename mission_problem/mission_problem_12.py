str1 = "성적을 입력하시오:"
str2 = "성적 평균은"
str3 = "입니다."
str4 = "80점 이상 성적을 받은 학생은"
str5 = "명입니다."


def mean(list):
    return sum(list) / len(list)


def over80(list):
    return len([i for i in list if i >= 80])


scoreList = list()

while True:
    score = int(input(str1))
    scoreList.append(score)

    if len(scoreList) >= 5:
        print(str2 + str(mean(scoreList)) + str3)
        print(str4 + str(over80(scoreList)) + str5)
        break
