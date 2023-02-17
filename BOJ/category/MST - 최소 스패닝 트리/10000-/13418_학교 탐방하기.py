# https://www.acmicpc.net/problem/13418

import sys

input = sys.stdin.readline


def mst(edges: list) -> int:
    def find_parent(x: int) -> int:
        if x != parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def merge(a: int, b: int) -> None:
        a = find_parent(a)
        b = find_parent(b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = [i for i in range(N + 1)]
    uphill = 0
    e = 0
    for edge in edges:
        C, A, B = edge

        if find_parent(A) != find_parent(B):
            merge(A, B)
            e += 1
            if C == 0:
                uphill += 1

            if e - 1 == N:
                break

    return uphill


N, M = map(int, input().split())
edges = []
A, B, C = map(int, input().split())  # 0 -> 1
k = 1 if C == 0 else 0
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

maxv = mst(sorted(edges)) + k
minv = mst(sorted(edges, reverse=True)) + k
print(maxv ** 2 - minv ** 2)


"""
13418. 학교 탐방하기
    - mst 두 번 돌리기
"""