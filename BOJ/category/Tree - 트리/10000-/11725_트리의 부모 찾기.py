# https://www.acmicpc.net/problem/11725

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def bfs(start: int) -> list:
    q = deque([start])
    parent = [-1] * (N + 1)

    while q:
        cur = q.popleft()

        for adj in tree[cur]:
            if adj == parent[cur]:
                continue
            q.append(adj)
            parent[adj] = cur

    return parent


def dfs(start: int) -> list:
    stack = [start]
    parent = [-1] * (N + 1)

    while stack:
        cur = stack.pop()

        for adj in tree[cur]:
            if adj == parent[cur]:
                continue
            stack.append(adj)
            parent[adj] = cur

    return parent


def dfs_recur(cur: int):
    for adj in tree[cur]:
        if adj == parent_recur[cur]:
            continue
        parent_recur[adj] = cur
        dfs_recur(adj)


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

parent_recur = [-1] * (N + 1)
# print(*bfs(1)[2:], sep="\n")
# print(*dfs(1)[2:], sep="\n")
dfs_recur(1)
print(*parent_recur[2:], sep="\n")