import sys
from collections import deque


def bfs(start, target):
    q = deque([(start, 0)])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        now, chon = q.popleft()

        if now == target:
            return chon

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, chon + 1))

    return -1


n = int(input())
start, target = map(int, input().split())
edge = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(edge):
    a, b = map(int, input().split())

    # undigraph
    graph[a].append(b)
    graph[b].append(a)


print(bfs(start, target))