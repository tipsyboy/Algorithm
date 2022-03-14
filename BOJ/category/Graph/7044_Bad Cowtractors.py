import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, edges):
    edges.sort(key=lambda x: -x[2])

    parent = [0] * (n + 1)
    for i in range(n + 1):
        parent[i] = i

    edge_count = 0
    rst = 0
    for edge in edges:
        a, b, cost = edge

        if find(parent, a) != find(parent, b):
            union(parent, a, b)

            edge_count += 1
            rst += cost

            if edge_count == n - 1:
                return rst

    if edge_count != n - 1:
        return -1


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())

    edges.append((a, b, c))

print(solution(n, edges))
