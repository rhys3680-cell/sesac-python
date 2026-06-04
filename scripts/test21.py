p0 = [2, 3]
ps = [[1, 1], [12, 13], [2, 5], [5, 6], [6, 7]]


def distance(p0, ps):
    # index이기 때문에 0으로 초기화
    sp = 0
    # index = 0에 해당하는 거리를 만들고 list에 저장
    initial_distance = ((ps[0][0] - p0[0]) ** 2 + (ps[0][1] - p0[1]) ** 2) ** 0.5
    dst_list = [initial_distance]

    # index = 1부터 비교해가면서 계산하고 0번째 거리보다 작은 값이 있으면 index와 값을 변수, 리스트에 저장
    for i, el in enumerate(ps[1:]):
        calc_distance = ((el[0] - p0[0]) ** 2 + (el[1] - p0[1]) ** 2) ** 0.5
        if initial_distance > calc_distance:
            initial_distance = calc_distance
            sp = i + 1

        dst_list.append(calc_distance)

    return sp, dst_list


print(distance(p0, ps))
