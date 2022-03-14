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


def solution(m, n):
    parent = [0] * m  # 0번 집부터 시작

    for i in range(m):
        parent[i] = i

    edges = []
    rst = 0
    mst_edges = 0

    for _ in range(n):
        a, b, cost = map(int, input().split())
        rst += cost
        edges.append((a, b, cost))

    # 그냥 sorting 하는 것보다 lambda식 써서 하는게 훨씬 빠른데 왜 그러지
    # edges.sort(key=lambda x: x[0])
    edges = sorted(edges, key=lambda x: x[2])

    for edge in edges:
        a, b, cost = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            rst -= cost

            # MST는 일종의 Tree 구조로 최종 간선의 개수가 (node개수 - 1)이므로 다 찾은 경우 더이상 찾을 필요가 없다.
            mst_edges += 1
            if mst_edges == m - 1:
                break

    return rst


while True:
    m, n = map(int, input().split())  # 집의 수 m, 노드 수 n

    if m == 0 and n == 0:
        break

    print(solution(m, n))
