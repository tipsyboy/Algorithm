#
INF = int(1e9)  # 무한대 설정

#
n, m = map(int, input().split())  # 노드, 간선 수

graph = [[INF] * (n + 1) for i in range(n + 1)]  # graph

# 자신에게 가는 길
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


# Floyd-Warshall
for via in range(1, n + 1):
    for start in range(1, n + 1):
        for to in range(1, n + 1):
            graph[start][to] = min(graph[start][to], graph[start][via] + graph[via][to])

print()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
