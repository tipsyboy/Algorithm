# 2024.11.28 THU
# https://www.acmicpc.net/problem/15681

import sys

sys.setrecursionlimit(10**5 + 5)
input = sys.stdin.readline


def dfs(cur):
    visited[cur] = True

    for sub in tree[cur]:
        if visited[sub]:
            continue
        node_cnt[cur] += dfs(sub)

    return node_cnt[cur]


N, R, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (N + 1)
node_cnt = [1] * (N + 1)
dfs(R)

ans = []
for _ in range(Q):
    u = int(input())
    ans.append(node_cnt[u])
print(*ans, sep="\n")
