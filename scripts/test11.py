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


# def check_member(name):
#     if name in members:
#         return name[:-2], name[-2:]
#     else:
#         return None, None


# sur, given = check_member("허찬빈")
# print(sur, given)


def check_member(name, age=20, gender="m"):
    sur = None
    given = None
    if name in members:
        if age > 30:
            sur, given = name[:-2], name[-2:] + "님"
        else:
            sur, given = name[:-2], name[-2:]
    else:
        sur, given = None, None

    return sur, given


sur, given = check_member("허찬빈", 32)
print(sur, given)

sur, given = check_member("한상훈")
print(sur, given)
