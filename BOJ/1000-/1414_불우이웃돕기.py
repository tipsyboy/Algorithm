# https://www.acmicpc.net/problem/1414

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
edges = []
total = 0
for u in range(N):
    conn = input().rstrip()

    for i in range(N):
        v = conn[i]
        if v == "0":
            continue

        if v.islower():
            edges.append((u, i, ord(v) - 96))
            total += ord(v) - 96
        else:
            edges.append((u, i, ord(v) - 38))
            total += ord(v) - 38
edges.sort(key=lambda x: x[2])

parent = [i for i in range(N)]
cnt, need = 0, 0
for edge in edges:
    u, v, c = edge

    if u == v:
        continue

    if find_parent(u, parent) == find_parent(v, parent):
        continue

    merge(u, v)
    cnt += 1
    need += c
    if cnt == N - 1:
        break

ans = 0
for i in range(N):
    if find_parent(i, parent) != 0:
        ans = -1
        break
if ans != -1:
    ans = total - need
print(ans)