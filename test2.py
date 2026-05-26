li1 = list(range(100))

li_e = list()
li_o = list()

for _ in range(len(li1)):
    item = li1.pop(0)
    if item % 2 == 0:
        li_e.append(item)
    else:
        li_o.append(item)

print(li_e)
print(li_o)
print(li1)
