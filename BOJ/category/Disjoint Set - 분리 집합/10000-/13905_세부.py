# 2025.02.12 WED
# https://www.acmicpc.net/problem/13905

import sys

input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
s, e = map(int, input().split())

bridges = []
for _ in range(M):
    h1, h2, k = map(int, input().split())
    bridges.append((h1, h2, k))
bridges.sort(key=lambda x: x[2], reverse=True)

parent = [i for i in range(N + 1)]
ans = 0
for h1, h2, k in bridges:

    if find_parent(h1) != find_parent(h2):
        union_parent(h1, h2)
        ans = k

    if find_parent(s) == find_parent(e):
        break

if find_parent(s) == find_parent(e):
    print(ans)
else:
    print(0)
