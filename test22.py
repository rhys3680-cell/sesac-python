t = "3141592"

p = "271"

# num = len(p)

# result = 0
# for i in range(len(t) - len(p) + 1):
#     substring = t[i : i + len(p)]

#     if p > substring:
#         result += 1

# print(result)


def solution(t, p):
    result = 0
    for i in range(len(t) - len(p) + 1):
        substring = t[i : i + len(p)]

        if p >= substring:
            result += 1

    return result


print(solution(t, p))
