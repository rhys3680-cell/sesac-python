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

a = ("은") in members[0]

# print(a)

# for m in members:
#     if m[0] == "김":
#         print(m)

# for m in members:
#     print(("은") in m)

# for i in range(len(members)):
#     for j in range(len(members[i])):
#         if members[i][j] == "은":
#             print(members[i])

# for m in members:
#     if m[0] in "남궁":
#         print(m)


for m, c in zip(members, check, strict=True):
    print(m, c)
