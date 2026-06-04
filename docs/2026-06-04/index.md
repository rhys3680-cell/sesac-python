1. 다차원 배열 속성 · 축 연산 (test27)

    ```python
    import numpy as np

    ndArr2 = np.arange(2 * 3 * 4 * 5).reshape(2, 3, 4, 5)

    ndArr2.ndim      # 4   (차원 수)
    ndArr2.shape     # (2, 3, 4, 5)
    ndArr2.size      # 120 (전체 원소 개수)
    ndArr2.dtype     # 자료형

    ndArr2.sum(axis=3)   # 마지막 축(크기 5)을 따라 합 → shape (2, 3, 4)
    ```

    - `ndim` / `shape` / `size` / `dtype`로 배열의 구조를 확인
    - `sum(axis=n)`은 지정한 축을 합치며 그 축이 사라짐 → 결과 차원이 하나 줄어듦

2. argmin · argsort 정렬 인덱스 (test31)

    ```python
    nd1 = np.array([5, 6, 4, 1, 2, 3])

    np.argmin(nd1)    # 3   (최솟값의 인덱스)
    np.argsort(nd1)   # [3 4 5 2 0 1]  (오름차순 정렬 순서의 인덱스)
    ```

    - `argmin`은 최솟값이 위치한 인덱스를 반환
    - `argsort`는 "정렬했을 때의 원소 인덱스 배열"을 반환 → 값이 아니라 순서를 알려줌

3. 벡터화 거리 계산 · 최근접 점 (test30 / test32)

    ```python
    pt = np.array([2, 3])
    ps = np.array([[2, 5], [5, 6], [6, 7]])

    def distance(pt: np.ndarray, ps: np.ndarray):
        dst = (((ps - pt) ** 2).sum(1)) ** 0.5   # 각 점까지의 유클리드 거리
        sp = np.argmin(dst)                       # 가장 가까운 점의 인덱스
        return ps[sp], dst[sp]
    ```

    - `ps - pt`는 브로드캐스팅으로 모든 점에서 한 번에 차이를 구함 (for문 불필요)
    - `.sum(1)`은 행별(축 1) 합 → 각 점의 제곱합, `** 0.5`로 거리
    - `argmin`으로 최소 거리 인덱스를 찾아 점·거리를 함께 반환
    - test30은 같은 계산을 벡터식 한 줄로, test32는 함수로 정리

4. 가중치 점수 랭킹 (test33 / test34)

    ```python
    names = np.array(["김", "이", "정"])
    scores = np.array([[90, 80, 70], [70, 80, 90], [100, 70, 70]])
    ratio = np.array([0.5, 0.3, 0.2])

    def wholePassed(names, scores, ratio, num=1):
        rank = np.argsort((scores * ratio).sum(1))[::-1][:num]
        return names[rank]
    ```

    - `scores * ratio`는 브로드캐스팅으로 과목별 가중치 적용, `.sum(1)`로 사람별 총점
    - `argsort(...)[::-1]`로 내림차순 인덱스, `[:num]`로 상위 num명 선택
    - `names[rank]`처럼 인덱스 배열로 이름을 한 번에 추출 (팬시 인덱싱)

5. 자료형 · 인덱스 형변환 (test35 / test36)

    ```python
    nd1 = np.array([1.0, 2, 3])   # 하나라도 float면 전체가 float64로 통일
    nd1.dtype                      # float64

    nd2 = np.array([5, 6, 7])
    nd2[int(nd1[0])]               # 인덱스는 정수여야 함 → int()로 변환 필요
    ```

    - NumPy 배열은 원소 자료형이 하나로 통일됨 (`1.0` 하나로 전체가 실수형)
    - 인덱스 자리에는 정수만 허용 → float 값은 `int()`로 변환 후 사용

6. 서버 증설 시뮬레이션 (test28 / test29)

    ```python
    # test29: 딕셔너리로 서버 수명(5틱) 관리
    for p in players:
        if math.floor(p / m) and not server.get(math.floor(p / m), False):
            server[math.floor(p / m)] = 5
        for k, v in server.items():
            server[k] = v - 1          # 매 틱 수명 감소
        key = math.floor(p / m)
        if key in server and server[key] == 0:
            del server[key]            # 수명 종료 시 제거
    ```

    - 동시 접속자(`players`) 기준으로 필요한 추가 서버 수를 시뮬레이션
    - test28: 리스트 + 카운터로 누적 증설량 계산
    - test29: 딕셔너리로 각 서버의 남은 수명을 틱 단위로 관리

7. 이미지 90도 회전 직접 구현 (test37)

    ```python
    from PIL import Image
    import numpy as np

    def rotate90_ccw(img_array: np.ndarray):
        h, w = img_array.shape[:2]
        out = np.zeros((w, h) + img_array.shape[2:], dtype=img_array.dtype)
        for y in range(h):
            for x in range(w):
                out[w - 1 - x, y] = img_array[y, x]   # 좌표 변환으로 픽셀 이동
        return out

    rotated = rotate90_ccw(np.array(Image.open(IMAGE_PATH)))
    Image.fromarray(rotated).show()
    ```

    - 회전 행렬 `[[0,-1],[1,0]]`에 해당하는 좌표 변환을 픽셀마다 적용
    - 출력 배열은 가로·세로가 뒤바뀐 `(w, h, 3)` 크기
    - 배열 인덱싱은 `[행, 열] = [y, x]` 순서라는 점에 주의 (`np.rot90`로 한 줄 대체 가능)

8. 두 이미지 평균 블렌딩 (test38)

    ```python
    h, w = img_array_1.shape[:2]
    img_array_2 = np.array(img2.resize((w, h)))   # PIL resize는 (너비, 높이) 순서

    # uint8(0~255) 오버플로우 방지를 위해 uint16으로 올려 계산
    blended = ((img_array_1.astype(np.uint16) + img_array_2.astype(np.uint16)) // 2).astype(np.uint8)
    Image.fromarray(blended).show()
    ```

    - 두 이미지를 더하려면 먼저 크기를 맞춰야 함 → `resize`로 통일
    - `uint8`은 255가 최대라 그냥 더하면 오버플로우 → `uint16`으로 변환 후 평균, 다시 `uint8`로
    - `shape`는 `(높이, 너비)`, `resize`는 `(너비, 높이)`로 순서가 반대
