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


def solution():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, cost = map(int, input().split())

        edges.append((a, b, cost))

    edges.sort(key=lambda x: x[2])

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    cost = 0
    mst_last_cost = 0
    count = 0
    for edge in edges:
        a, b, c = edge

        # 받은 두 도시의 부모노드가 같지 않다 -> 아직 연결되지 않은 집합 -> 사이클 x
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cost += c
            count += 1
            mst_last_cost = c

        if count == n - 1:
            break

    return cost - mst_last_cost


print(solution())


"""
1647. 도시 분할 계획 (Gold 4)
    - 크루스칼 알고리즘 기본 예제 공식처럼 적용하면 된다. greedy 
    
    - 두 도시의 노드가 아직 연결되어 있지 않다는 뜻은 무방향 그래프에서 사이클이 없다는 말과 같으므로
      find 연산을 통해서 사이클 확인을 해주고 union한다. 

    - MST에서 edge의 개수는 node개수-1 이므로 edges 탐색중에 모든 간선을 찾으면 break 한다. 
"""