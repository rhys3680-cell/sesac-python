1. enumerate
    
    ```python
    people_one = list()
    people_zero = list()
    
    for i, c in enumerate(check):
        if check[i] == 1:
            people_one.append(members[i])
        else:
            people_zero.append(members[i])
    
    print(people_one)
    print(people_zero)
    ```
    
2. zip
    
    ```python
    for m in members:
        if m[0] == "김":
            print(m)
    
    for m in members:
        print(("은") in m)
    
    for i in range(len(members)):
        for j in range(len(members[i])):
            if members[i][j] == "은":
                print(members[i])
    
    for m in members:
        if m[0] in "남궁":
            print(m)
    
    for m, c in zip(members, check, strict=True):
        print(m, c)
    
    ```
    
3. count 메서드와 for문 비교1
    
    ```python
    cnt = 0
    for word in MY_SONG.split():
        if ("그대") in word:
            # print(word)
            cnt += 1
    
    print(cnt)
    
    cnt2 = MY_SONG.count("그대")
    
    print(cnt2)
    ```
    
4. count 메서드와 for문 비교2
    
    ```python
    words = ["별", "그대", "시", "기억"]
    
    # for word in words:
    #     print(word)
    
    for idx in range(len(MY_SONG)):
        one_word = MY_SONG[idx : (idx + 1)]
        two_word = MY_SONG[idx : (idx + 2)]
    
        if one_word == words[0]:
            print(one_word)
        elif two_word == words[1]:
            print(two_word)
        elif one_word == words[2]:
            print(one_word)
        elif two_word == words[3]:
            print(two_word)
    
    for word in words:
        print(MY_SONG.count(word))
    
    ```
    
5. dict 메서드
    
    ```python
    dict1 = {"별": 1, "그대": 7, "시": 3, "기억": 3}
    
    # print(dict1["별"])
    
    # print(dict1.get("별"))
    
    # print(hash("python"))
    
    # NOTE: get일 경우 return 시 None 혹은 내가 원하는 값 반환 가능, 더 안정적인 코드 운영 가능
    # print(dict1.get(0))
    
    # print(dict1.keys())
    
    # print(dict1.items())
    
    # print(dict1.values())
    
    # for k, v in dict1.items():
    #     print(k, v)
    
    for kv in dict1.items():
        print(kv[0], kv[1])
    
    ```
    
6. 함수 정의 및 활용
    
    ```python
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
    
    ```