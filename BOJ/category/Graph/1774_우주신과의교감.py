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


def get_dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def kruskal(n, m):
    parent = [i for i in range(n + 1)]
    coord = []  # 모든 별의 좌표
    edges = []  # 모든 간선
    mst_edges_count = 0  # MST 간선 개수
    rst = 0

    # 좌표 입력
    for _ in range(n):
        x, y = map(int, input().split())
        coord.append((x, y))

    # 모든 거리 계산
    for i in range(n - 1):
        for j in range(i + 1, n):
            dist = get_dist(coord[i][0], coord[i][1], coord[j][0], coord[j][1])
            edges.append((i + 1, j + 1, dist))

    edges.sort(key=lambda x: x[2])

    # 이미 연결된 간선 연결하기
    for _ in range(m):
        a, b = map(int, input().split())

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            mst_edges_count += 1

    # 전체 간선 확인
    for edge in edges:
        a, b, cost = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            rst += cost
            mst_edges_count += 1

            if mst_edges_count == n - 1:
                break

    return rst


n, m = map(int, input().split())
print("{:.2f}".format(kruskal(n, m)))
