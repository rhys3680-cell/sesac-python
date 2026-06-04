1. 부분 문자열 사전순 비교 (test21 / test23)

    ```python
    def solution(t, p):
        result = 0
        for i in range(len(t) - len(p) + 1):
            substring = t[i : i + len(p)]
            if p >= substring:
                result += 1
        return result
    ```

    - 슬라이딩 윈도우로 길이 `len(p)`짜리 부분 문자열을 차례로 잘라냄
    - 부분 문자열 개수는 `len(t) - len(p) + 1`개
    - 같은 길이의 숫자 문자열은 사전순(`>=`) 비교가 정수 비교와 동일 → `int()` 변환 없이도 동작 (test21은 `int` 변환, test23은 문자열 비교로 같은 결과)

2. 최근접 점 탐색 (test20)

    ```python
    def distance(p0, ps):
        sp = 0  # 가장 가까운 점의 인덱스
        initial_distance = ((ps[0][0] - p0[0]) ** 2 + (ps[0][1] - p0[1]) ** 2) ** 0.5
        dst_list = [initial_distance]

        for i, el in enumerate(ps[1:]):
            calc_distance = ((el[0] - p0[0]) ** 2 + (el[1] - p0[1]) ** 2) ** 0.5
            if initial_distance > calc_distance:
                initial_distance = calc_distance
                sp = i + 1
            dst_list.append(calc_distance)

        return sp, dst_list
    ```

    - 기준점 `p0`에서 각 점까지의 유클리드 거리를 계산
    - 0번째 거리로 최소값을 초기화한 뒤 1번째부터 순회하며 갱신
    - `enumerate(ps[1:])`는 인덱스가 0부터 시작하므로 실제 인덱스는 `i + 1`

3. NumPy 배열 생성·연결·연산 (test22)

    ```python
    import numpy as np

    range_array = np.arange(10)                    # [0 1 2 ... 9]

    x = np.array([[1, 1], [2, 2]])
    y = np.array([[5, 6]])
    z = np.concatenate((x, y), axis=0)             # 행 방향으로 결합

    mat1 = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
    unit_matrix = np.eye(3)                         # 단위행렬
    np.dot(mat1, unit_matrix)                       # 행렬 곱
    mat1.max(axis=0)                                # 열별 최댓값

    data2 = np.array([[1, 2], [3, 4], [5, 6]])
    data2 + np.array([[1, 1]])                       # 브로드캐스팅
    ```

    - `np.arange` / `np.array`로 배열 생성, `np.concatenate(axis=)`로 결합 축 지정
    - `np.dot`은 행렬 곱, 단위행렬과 곱하면 원본 유지
    - `axis=0`은 행을 가로질러(열별), `axis=1`은 열을 가로질러(행별) 연산
    - 모양이 다른 배열도 규칙에 맞으면 자동 확장되는 **브로드캐스팅** 지원

4. reshape · 인덱싱 / 슬라이싱 (test24)

    ```python
    nd1 = np.arange(12).reshape(3, 4)

    nd1.shape        # (3, 4)
    nd1[1][2]        # 6  (2번째 행, 3번째 열)
    nd1[1:, :]       # 1번 행부터 끝까지 전체 열
    nd1[:, 1:2]      # 모든 행, 1번 열만 (2차원 유지)
    nd1[1:, 2:]      # 1번 행 이후 & 2번 열 이후의 부분 행렬
    ```

    - `reshape(행, 열)`로 1차원 배열을 다차원으로 재구성
    - `[행_슬라이스, 열_슬라이스]` 형태로 행·열을 동시에 슬라이싱
    - `nd1[:, 1:2]`처럼 슬라이스를 쓰면 차원이 유지되고, `nd1[:, 1]`은 차원이 줄어듦

5. 축별 통계 함수 (test25)

    ```python
    nd1 = np.arange(12).reshape(3, 4)

    np.mean(nd1)           # 전체 평균
    np.mean(nd1, axis=0)   # 열별 평균
    np.mean(nd1, axis=1)   # 행별 평균
    np.median(nd1, axis=0) # 열별 중앙값
    np.median(nd1, axis=1) # 행별 중앙값
    ```

    - `axis`를 생략하면 전체, `axis=0`은 열별, `axis=1`은 행별 집계
    - `mean`(평균) / `median`(중앙값) 모두 동일한 축 규칙을 따름

6. 불리언 마스킹 · 팬시 인덱싱 (test26)

    ```python
    nd1 = np.arange(12).reshape(3, 4)

    nd1 > 4                 # 각 원소에 대한 True/False 배열
    nd1[nd1 > 4]            # 조건을 만족하는 원소만 1차원으로 추출
    nd1[[True, False, False], :2]   # 0번 행 선택 + 앞 2개 열
    nd1[[False, True, True]][:, [False, False, True, True]]  # 행/열 각각 불리언 선택
    ```

    - **불리언 마스킹**: 비교 연산으로 만든 True/False 배열로 조건에 맞는 원소만 골라냄
    - **팬시 인덱싱**: 불리언 리스트로 특정 행·열을 선택 (행 선택 후 다시 열 선택 가능)