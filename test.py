li1 = range(100)


# for i in li1:
#     if i % 2 == 0:
#         li_e.append(i)
#     else:
#         li_o.append(i)


def oddListAndEvenList(list):
    return [i for i in list if i % 2 == 0], [i for i in list if i % 2 != 0]


li_e, li_o = oddListAndEvenList(li1)

print(li_e)
print(li_o)
