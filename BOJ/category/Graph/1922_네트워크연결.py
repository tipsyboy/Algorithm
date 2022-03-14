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


def kruskal(n, m):
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n + 1)]
    rst = 0
    mst_edges_count = 0

    for edge in edges:
        a, b, cost = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            rst += cost
            mst_edges_count += 1

            if mst_edges_count == n - 1:
                break

    return rst


n = int(input())
m = int(input())

print(kruskal(n, m))
