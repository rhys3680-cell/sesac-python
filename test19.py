lottos = [0, 0, 0, 0, 0, 0]
win_nums = [31, 10, 45, 1, 6, 19]

# zero_count + same_number: 맞힌 갯수


def solution(lottos: list, win_nums: list) -> list:

    dict1 = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6}

    zero_count = lottos.count(0)

    same_number = set(lottos).intersection(win_nums)

    sum = zero_count + len(same_number)

    a = 6 if dict1[sum] + zero_count == 7 else dict1[sum] + zero_count

    return [dict1[sum], a]


def solution2(lottos: list, win_nums: list) -> list:
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}  # 맞힌 개수 -> 순위
    zero_count = lottos.count(0)
    match_count = len(set(lottos) & set(win_nums) - {0})

    max_match = match_count + zero_count  # 0이 전부 당첨이라 가정 (최고)
    min_match = match_count  # 0이 전부 꽝이라 가정 (최저)

    return [rank.get(max_match, 6), rank.get(min_match, 6)]


print(solution(lottos, win_nums))
