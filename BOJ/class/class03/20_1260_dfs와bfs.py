import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

# init graph
for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

# graph sorting
for i in range(1, len(graph)):
    graph[i].sort()

visited = [False] * (n+1)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)


def bfs(graph, v):
    visited = [False] * (n+1)
    q = deque([v])
    visited[v] = True

    print(v, end=" ")

    while q:
        now = q.popleft()

        for node in graph[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                print(node, end=" ")


dfs(graph, v, visited)
print()
bfs(graph, v)
