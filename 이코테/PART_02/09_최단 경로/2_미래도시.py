#
INF = int(1e9)

# node, edge
n, m = map(int, input().split())

# graph
graph = [[INF] * (n + 1) for i in range(n + 1)]

# 자신으로 가는 거리
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

# 그래프 간선 연결
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1  # 모든 노드 간의 거리 비용은 1로 동일하다.

x, k = map(int, input().split())  # x: 도착지, k: 경유지

# Floyd-warshall
for via in range(1, n + 1):
    for start in range(1, n + 1):
        for to in range(1, n + 1):
            graph[start][to] = min(graph[start][to], graph[start][via] + graph[via][to])

distance = graph[1][k] + graph[k][x]

#
print()
if distance >= INF:
    print("-1")
else:
    print(distance)
