# https://www.acmicpc.net/problem/1240

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start: int, dest: int) -> int:
    q = deque([(start, 0)])
    visited = [False] * (N + 1)
    visited[start] = True

    while q:
        cur, dist = q.popleft()

        if cur == dest:
            return dist

        for adj, w in tree[cur]:
            if visited[adj]:
                continue

            q.append((adj, dist + w))
            visited[adj] = True

    return -1


N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, d = map(int, input().split())
    tree[u].append((v, d))
    tree[v].append((u, d))

for _ in range(M):
    u, v = map(int, input().split())
    print(bfs(u, v))