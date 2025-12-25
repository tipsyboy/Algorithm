# https://www.acmicpc.net/problem/4195

import sys

input = sys.stdin.readline


def get_number(name: str, names_num: dict) -> int:
    global nxt_num

    if name not in names_num:
        names_num[name] = nxt_num
        parent.append(nxt_num)
        networks.append(1)
        nxt_num += 1

    return names_num[name]


def find_parent(x: int, parent: list) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)

    return parent[x]


def merge(a: int, b: int) -> None:
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a < b:
        parent[b] = a
        networks[a] += networks[b]
    else:
        parent[a] = b
        networks[b] += networks[a]


TC = int(input())
for _ in range(TC):
    F = int(input())

    parent = []
    networks = []
    nxt_num = 0
    names_num = dict()

    for __ in range(F):
        f1, f2 = input().split()

        u, v = get_number(f1, names_num), get_number(f2, names_num)
        a, b = find_parent(u, parent), find_parent(v, parent)
        if a != b:
            merge(a, b)

        print(max(networks[a], networks[b]))