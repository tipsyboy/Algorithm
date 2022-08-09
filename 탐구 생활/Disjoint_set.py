"""
    서로소 집합(Disjoint set)
    같은 부모를 갖고 있는 (다른 조건이 없으면 관습적으로 작은 번호의 노드가 부모가 됨) 집합 요소를
    구분하는 알고리즘? 자료구조.
"""
import sys
input = sys.stdin.readline

# def find_parent(parent, node):
#     if node != parent[node]:
#         return find_parent(parent, parent[node])

#     return node


# 경로 압축 기법
def find_parent(parent, node):
    if node != parent[node]:
        parent[node] = find_parent(parent, parent[node])

    return parent[node]


def union_parent(parent, a, b):
    # node a, b의 부모 노드 찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# node와 edge 수 입력 받기
v, e = map(int, input().split())  # node, edge
parent = [0] * (v+1)  # init parent list

# init parent table
for i in range(1, v+1):
    parent[i] = i


# 간선 연결
for i in range(e):
    a, b = map(int, input().split())  # 두 노드 받아서

    union_parent(parent, a, b)

# 이 과정이 union 이후에 자신의 루트노드로 parent[]를 최신화한다.
for i in range(1, v + 1):
    find_parent(parent, i)
