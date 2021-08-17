import sys

input = sys.stdin.readline


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            graph[i][j] = graph[i][j] + graph[i - 1][j]
        elif j == i:
            graph[i][j] = graph[i][j] + graph[i - 1][j - 1]
        else:
            graph[i][j] = max(graph[i - 1][j - 1], graph[i - 1][j]) + graph[i][j]

print(max(graph[n - 1]))
