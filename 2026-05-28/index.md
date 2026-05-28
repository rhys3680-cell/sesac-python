1. 함수
    1. 모듈화의 기본 def 예약어로 선언
    
    ```python
    def my_func():
    	a = 5
    	print(a)
    	
    # 5
    ```
    
2. 딕셔너리
    1. 키 밸류로 이루어진 자료구조
    
    ```python
    dict1 = {}
    
    print(dict1.keys()) # 키를 가져옴 
    print(dict1.values()) # 값을 가져옴
    print(dict1.items()) # 키와 값을 list[tuple] 형태로 반환
    ```
    
3. str 메서드
    
    ```python
    str1 = "Hello World"
    
    str1.split() # sep을 파라미터로 받아 기준으로 절삭
    str1.find('a') # a를 찾아 갯수를 반환
    str1.replace('Hello', 'hello') # 파라미터를 두 개를 받아 변환
    str1.upper() # 대문자로 변환
    str1.lower() # 소문자로 변환
    str1.startswith("Hello") # 파라미터로 시작하는지
    str1.endswith("World") # 파라미터로 끝나는지 
    ```
    
4. 문제 풀이
    
    ```python
    # 다음을 만족하는 함수를 작성하시오.
    # 1. space 기준으로 word 를 구분하고
    # 2. 3글자 이하는 제외하고
    # 3. 가장 많이 나오는 단어 Top 10 을 return 해주는 함수
    # 실행예시
    # print(top_ten_word(msg))
    # 출력예시
    # ['will','that','have','freedom','from','Negro','with','this','come','every']
    
    def solution(msg):
        words = set([word for word in msg.split() if len(word) > 4])
        ranking = {}
        for word in words:
            ranking[word] = msg.count(word)
    
        return sorted(ranking.items(), key=lambda kv: -kv[1])[:10]
    ```


미션 문제 해답
https://github.com/rhys3680-cell/sesac-python