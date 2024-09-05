# 2024.08.30 FRI
# https://www.acmicpc.net/problem/13265

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        cur = q.popleft()

        for adj in graph[cur]:
            if visited[adj] != -1:
                if visited[cur] == visited[adj]:
                    return False
            else:
                visited[adj] = visited[cur] ^ 1
                q.append(adj)

    return True


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for __ in range(n + 1)]
    visited = [-1] * (n + 1)
    for __ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    ans = "possible"
    for i in range(1, n + 1):
        if visited[i] == -1 and not bfs(i):
            ans = "impossible"

    print(ans)
