from collections import Counter


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

    return parent


def solution(n, computers):
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and find(parent, i) != find(parent, j):
                parent = union(parent, i, j)

    for i in range(n):
        find(parent, i)

    return len(Counter(parent))
    