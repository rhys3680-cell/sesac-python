t = "3141592"
p = "271"


def solution(t, p):
    substring_number = len(t) - len(p) + 1

    return len(
        [
            int(p) >= int(t[i : i + len(p)])
            for i in range(substring_number)
            if int(p) >= int(t[i : i + len(p)])
        ]
    )


print(solution(t, p))
