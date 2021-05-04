import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def solution1():
    # bfs로 풀이
    n, m = map(int, input().split())
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]

    # init graph
    for _ in range(m):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    count = 0
    for i in range(1, len(visited)):
        if not visited[i]:
            q.append(i)
            visited[i] = True

            while q:
                now = q.popleft()

                for node in graph[now]:
                    if not visited[node]:
                        q.append(node)
                        visited[node] = True

            count += 1

    print(count)


def solution2():
    # dfs 구현
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n+1)]
    count = 0

    # init graph
    for _ in range(m):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    def dfs(garph, v, visited):
        visited[v] = True

        for node in graph[v]:
            if not visited[node]:
                dfs(graph, node, visited)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1

    print(count)


def solution3():
    n, m = map(int, input().split())
    parent = [0] * (n+1)

    # init parent list
    for i in range(1, n+1):
        parent[i] = i

    # 부모 노드 찾기 - 경로 압축 기법
    def find_parent(parent, node):
        if node != parent[node]:
            parent[node] = find_parent(parent, parent[node])

        return parent[node]

    # 간선 연결하기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    # 간선 받으면서 결합
    for _ in range(m):
        a, b = map(int, input().split())

        union_parent(parent, a, b)

    # 최종 부모노드(루트) 찾기
    for i in range(1, n+1):
        find_parent(parent, i)

    print(len(set(parent)) - 1)


# solution1()  # bfs 구현
# solution2()  # dfs 구현
solution3()  # 서로소 집합(Disjoint Set)을 이용한 구현
