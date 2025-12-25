# https://www.acmicpc.net/problem/10216

import sys
from math import sqrt

input = sys.stdin.readline


def find_parent(x: int) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_node(a: int, b: int) -> None:
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def is_possible(p: int, q: int) -> bool:
    # dist = (((nodes[p][0] - nodes[q][0]) ** 2) + ((nodes[p][1] - nodes[q][1]) ** 2)) ** 0.5
    dist = sqrt(((nodes[p][0] - nodes[q][0]) ** 2) + ((nodes[p][1] - nodes[q][1]) ** 2))
    return dist <= nodes[p][2] + nodes[q][2]


TC = int(input())
for _ in range(TC):
    N = int(input())

    nodes = [tuple(map(int, input().split())) for _ in range(N)]
    parent = [i for i in range(N)]

    for i in range(N - 1):
        for j in range(i + 1, N):
            if is_possible(i, j):
                union_node(i, j)

    rst = set()
    for i in range(N):
        rst.add(find_parent(i))
    print(len(rst))
