members = [
    "김찬은",
    "송문택",
    "윤창기",
    "최진주",
    "류경혜",
    "김진경",
    "최호연",
    "노현동",
    "배원준",
    "정선영",
    "민승희",
    "임지수",
    "안지예",
    "김민주",
    "한예진",
    "유은영",
    "김인석",
    "이수인",
    "정종현",
    "허찬빈",
    "진혜원",
    "남궁세정",
]

check = [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1]

people_one = list()
people_zero = list()

for i, c in enumerate(check):
    if check[i] == 1:
        people_one.append(members[i])
    else:
        people_zero.append(members[i])

print(people_one)
print(people_zero)
