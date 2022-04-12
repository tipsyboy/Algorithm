import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


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


def solution():
    n, m = map(int, input().split())  # node-1 수, command 수
    parent = [0] * (n + 1)

    # init parent table
    for i in range(n + 1):
        parent[i] = i

    for _ in range(m):
        com, a, b = map(int, input().split())

        if com == 0:  # union 연산
            union_parent(parent, a, b)
        elif com == 1:  # check 연산
            if find_parent(parent, a) != find_parent(parent, b):
                print("NO")
            else:
                print("YES")


solution()


"""
1717. 집합의 표현 (Gold 4)
    -
    
"""