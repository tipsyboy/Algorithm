import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def mst(v, e):
    parent = [i for i in range(v + 1)]
    edges = []
    rst = 0

    for _ in range(e):
        a, b, c = map(int, input().split())

        edges.append((a, b, c))

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        a, b, cost = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            rst += cost

    return rst


v, e = map(int, input().split())

print(mst(v, e))
