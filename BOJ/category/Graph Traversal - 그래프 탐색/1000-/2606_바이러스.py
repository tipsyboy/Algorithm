import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(node, graph, visited):
    visited[node] = True

    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj, graph, visited)

    return visited


def solution1():
    n = int(input())
    m = int(input())  # 간선
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())

        # undi graph
        graph[a].append(b)
        graph[b].append(a)

    visited = dfs(1, graph, visited)

    count = 0
    for i in range(1, n + 1):
        if visited[i]:
            count += 1

    return count - 1


def bfs(start, n, graph):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    count = 0

    while q:
        now = q.popleft()

        for adj in graph[now]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True
                count += 1

    return count


def solution2():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    return bfs(1, n, graph)


# print(solution1())
print(solution2())
