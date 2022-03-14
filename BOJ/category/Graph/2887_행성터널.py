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


def kruskal(n):
    parent = [i for i in range(n)]
    mst_edges_count = 0
    rst = 0

    # 각 행성의 좌표 입력
    edges = []
    x = []
    y = []
    z = []

    for i in range(n):
        x_coord, y_coord, z_coord = map(int, input().split())

        x.append((x_coord, i))
        y.append((y_coord, i))
        z.append((z_coord, i))

    x.sort(key=lambda x: x[0])
    y.sort(key=lambda x: x[0])
    z.sort(key=lambda x: x[0])

    for i in range(n - 1):
        edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
        edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
        edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

    edges.sort(key=lambda x: x[0])

    for edge in edges:
        dist, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            rst += dist

            mst_edges_count += 1
            if mst_edges_count == n - 1:
                break

    return rst


n = int(input())

print(kruskal(n))