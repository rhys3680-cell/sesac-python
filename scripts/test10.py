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
