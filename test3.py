scores = [[70, 80, 90], [50, 40, 20], [70, 50, 80]]


def mean(list):
    return round(sum(list) / len(list), 2)


meanList = list()

for stdnt in scores:
    meanList.append(mean(stdnt))


print(meanList)
