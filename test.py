li1 = range(100)


# for i in li1:
#     if i % 2 == 0:
#         li_e.append(i)
#     else:
#         li_o.append(i)


# MEMO: 리스트 컴프리헨션은 스크립터에서 기계어로 바로 실행되기 때문에 for문보다 훨씬 빠름
def oddListAndEvenList(list):
    return [i for i in list if i % 2 == 0], [i for i in list if i % 2 != 0]


li_e, li_o = oddListAndEvenList(li1)

print(li_e)
print(li_o)
