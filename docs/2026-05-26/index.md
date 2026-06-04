# Wrap-Up

1. 파이썬
    1. 파이썬은 인터프리터 언어
        1. 메모리 부담 있음
    2. 다양한 라이브러리, 쉬운 문법으로 진입장벽 낮음
2. 변수
    1. 값을 저장하는 그릇
    2. 값을 바꿀 경우, 가리키는 메모리 주소를 변경함
    3. 파이썬에서는 타입이 유연함
    4. 이전에는 미리 선언된 변수 타입에 따라 고정되었음
    5. 하지만 이후에는 고정시키고 싶어질 때가 있을 것으로 예상
    6. 참고 코드
    
    ```python
    a = 123
    
    a = 345
    
    a = "Hello World"
    ```
    
3. 조건문
    1. 주어진 조건의 True, False 여부에 따라 특정 동작 수행
    2. 참고 코드
    
    ```python
    n = int(input("정수를 입력해주세요: "))
    
    if n % 2 == 0:
    	print("짝수입니다.")
    else:
    	print("홀수입니다.")
    ```
    
4. 반복문
    1. 특정 동작을 반복시키고 싶을 때 사용
    
    ```python
    sum = 0
    for i in range(1, 11):
    	sum += i
    	
    # 55
    ```
    
5. 자료구조
    1. list
        1. 값이 변하는 자료구조
        
        ```python
        li1 = [1, 2, 3]
        ```
        
    2. tuple
        1. 값이 안 변하는 자료구조
        
        ```python
        tp1 = (1, 2, 3)
        ```
        
    3. dictionary
        1. key, value로 이루어진 자료구조
        
        ```python
        dict1 = {"a" : 1, "b": 2, "c": 3}
        ```
        
6. 인덱싱과 슬라이싱
    1. 인덱싱: 특정 위치의 요소 추출
    2. 슬라이싱: 연속된 범위의 요소들을 추출
    
    ```python
    text = "python"
    
    print(text[0])
    print(text[1])
    # print(text[100]) Index 에러
    
    print(text[0:2])
    print(text[0:100])
    ```
    
7. 성능 최적화
    
    ```python
    li1 = list(range(100))
    
    li_e = list()
    li_o = list()
    
    # MEMO: 원본 배열을 변경시켜 메모리 부담을 완화
    for _ in range(len(li1)):
        item = li1.pop(0)
        if item % 2 == 0:
            li_e.append(item)
        else:
            li_o.append(item)
    
    print(li_e)
    print(li_o)
    print(li1)
    ```
    
8. 파이써닉 문법
    1. 리스트 컴프리헨션
    
    ```python
    li1 = range(100)
    
    # for i in li1:
    #     if i % 2 == 0:
    #         li_e.append(i)
    #     else:
    #         li_o.append(i)
    
    # MEMO: 리스트 컴프리헨션은 스크립터에서 기계어로 바로 실행되기 때문에 for문보다 훨씬 빠름
    def oddListAndEvenList(list):
        return [i for i in list if i % 2 == 0], [i for i in list if i % 2 != 0]
    
    li_e, li_o = oddListAndEvenList(li1)
    
    print(li_e)
    print(li_o)
    
    ```
    
9. 문자열 다루기
    
    ```python
    # 문자열은 immutable한 list, 즉 튜플임
    # pop(), remove() 안됨
    # 문자열 핸들링하는 함수가 많음
    
    str1 = "Good Morning ~~~ !!!"
    str2 = "SH Han"
    
    print(str1 + str2)
    
    ```