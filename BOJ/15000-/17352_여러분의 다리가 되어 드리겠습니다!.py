# https://www.acmicpc.net/problem/17352

import sys

input = sys.stdin.readline


def find_parent(x: int, parent: list) -> int:
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def merge(u: int, v: int) -> None:
    u = find_parent(u, parent)
    v = find_parent(v, parent)

    if u < v:
        parent[v] = u
    else:
        parent[u] = v


N = int(input())
parent = [i for i in range(N + 1)]
for _ in range(N - 2):
    a, b = map(int, input().split())

    if find_parent(a, parent) != find_parent(b, parent):
        merge(a, b)


ans = [-1, -1]
ans[0] = parent[1]
for i in range(2, N + 1):
    if ans[0] != find_parent(i, parent):
        ans[1] = parent[i]
        break
print(*ans)