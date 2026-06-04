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
