import math


players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
m = 3
k = 5

server = {}


for p in players:
    if math.floor(p / m) and not server.get(math.floor(p / m), False):
        server[math.floor(p / m)] = 5

    for k, v in server.items():
        server[k] = v - 1

    key = math.floor(p / m)

    if key in server and server[key] == 0:
        del server[key]

    print(p, key, server)
