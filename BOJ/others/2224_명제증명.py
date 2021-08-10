import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[INF] * (52) for _ in range(52)]

for _ in range(n):
    proposition = input().rstrip()
    ant = proposition[0]
    con = proposition[5]
    if ant.isupper():
        ant = ord(ant) - 65
    else:
        ant = ord(ant) - 97 + 26

    if con.isupper():
        con = ord(con) - 65
    else:
        con = ord(con) - 97 + 26

    graph[ant][con] = 1

for i in range(52):
    graph[i][i] = 0

for k in range(52):
    for i in range(52):
        for j in range(52):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

rst = []
for i in range(52):
    for j in range(52):
        if i == j:
            continue

        if graph[i][j] != INF:
            rst.append((i, j))

print(len(rst))
for a, b in rst:
    if a < 26:
        ant = chr(a + 65)
    else:
        ant = chr(a + 97 - 26)

    if b < 26:
        con = chr(b + 65)
    else:
        con = chr(b + 97 - 26)

    print(f"{ant} => {con}")

"""
    sibal
"""