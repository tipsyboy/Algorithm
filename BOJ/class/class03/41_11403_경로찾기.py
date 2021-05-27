import sys
from collections import deque
input = sys.stdin.readline


# 1) Floyd-Warshall 풀이
def floyd_warshall():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    for k in range(n):  # k: 거쳐가는 지점
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

    # print(graph)
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=" ")
        print()


# 2) dfs로 풀이
def dfs_algo():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    # dfs 수행
    def dfs(node):
        for i in range(n):
            if not visited[i] and graph[node][i] == 1:
                visited[i] = 1  # 방문 처리
                dfs(i)

    visited = [0] * n  # 방문 배열 초기화
    rst = []
    for i in range(n):
        dfs(i)  # 현재 노드에서 갈 수 있는 노드를 찾기 위해서 dfs()를 수행하고
        rst.append(visited)  # 결과 list가 현재 노드 i에서 갈 수 있는 node들을 의미함
        visited = [0] * n  # 방문 배열 초기화

    # print
    for i in range(n):
        for j in range(n):
            print(rst[i][j], end=" ")
        print()


# 3) bfs로 풀이
def bfs_algo():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    def bfs(start):
        visited = [0 for _ in range(n)]
        q = deque([start])

        while q:
            now = q.popleft()

            for i in range(n):
                if not visited[i] and graph[now][i] == 1:
                    visited[i] = 1
                    q.append(i)

        return visited

    rst = []  # 결과
    for i in range(n):
        rst.append(bfs(i))

    for i in range(n):
        for j in range(n):
            print(rst[i][j], end=" ")
        print()


bfs_algo()


"""
41. 11403 경로 찾기 (silver 1)
    - Floyd-warshall / dfs / bfs로 각각 풀어 보았다.
      가장 먼저 생각 났던 방법인 플로이드 워셜 알고리즘의 경우가 가장 간단하게 코드를 작성할 수 있었으나, 
      O(n^3)의 시간복잡도를 갖기 때문에 나머지 방법에 비해서 시간 복잡도가 높게 측정되었다. 

    - dfs / bfs의 경우 계속 공부해야 할 문제들이기 때문에 연습차 했는데, 
      처음에는 약간 헷갈렸으나 현재 노드와 다음 노드로 가는 방향성만 
      생각 한다면 쉽게 풀 수 있었던 것 같다.
"""
