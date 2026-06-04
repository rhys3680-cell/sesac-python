import math


players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
m = 3
k = 5

isOn = False
timeCnt = 0
cnt = 0
arr = []
additionalServerCnt = 0

for p in players:
    if math.floor(p / m) > 0 and isOn is False:
        isOn = True

    if isOn:
        timeCnt += 1
        arr.append(math.floor(p / m))
        if max(arr) > additionalServerCnt:
            cnt += max(arr) - additionalServerCnt
        additionalServerCnt = max(arr)

    print(
        p,
        isOn,
        timeCnt,
        math.floor(p / m),
        arr,
        timeCnt == k,
        additionalServerCnt,
    )

    if timeCnt == k:
        isOn = False
        timeCnt = 0
        additionalServerCnt = 0
        arr.clear()


print(cnt)


# def solution(players, m, k):
#     isOn = False
#     timeCnt = 0
#     cnt = 0
#     arr = []

#     for p in players:
#         if math.floor(p / m) > 0 and isOn is False:
#             isOn = True

#         if isOn:
#             timeCnt += 1
#             arr.append(math.floor(p / m))

#         if timeCnt == k:
#             isOn = False
#             timeCnt = 0
#             cnt += max(arr)
#             arr.clear()

#     return cnt


# print(solution(players, m, k))
