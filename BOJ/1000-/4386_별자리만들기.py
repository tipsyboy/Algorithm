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


def cal_dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def solution():
    n = int(input())

    star_pos = []
    for _ in range(n):
        x, y = map(float, input().split())

        star_pos.append((x, y))

    parent = [0] * n
    for i in range(n):
        parent[i] = i

    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            cost = cal_dist(
                star_pos[i][0], star_pos[i][1], star_pos[j][0], star_pos[j][1]
            )
            edges.append((i, j, cost))
    edges.sort(key=lambda x: x[2])

    mst_cost = 0
    mst_count = 0
    for edge in edges:
        a, b, cost = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            mst_cost += cost
            mst_count += 1

            if mst_count == n - 1:
                break

    return mst_cost


print("%.2f" % solution())
