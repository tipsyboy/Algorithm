# https://www.acmicpc.net/problem/5567

import sys
from collections import deque

input = sys.stdin.readline


def bfs(n: int, start: int) -> int:
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    lv, ans = 0, 0
    while q:
        if lv > 1:
            break
        for _ in range(len(q)):
            now = q.popleft()

            for adj in graph[now]:
                if visited[adj]:
                    continue

                q.append(adj)
                visited[adj] = True
                ans += 1

        lv += 1

    return ans


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(n, 1))