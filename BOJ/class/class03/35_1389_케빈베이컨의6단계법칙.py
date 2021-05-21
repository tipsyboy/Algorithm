import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)


# 1) Floyd-Washall Algorithm
def floyd_warshall():
    n, m = map(int, input().split())  # node, edge
    rst = [INF, INF]  # user, user_sum

    # 1) init graph
    graph = [[INF] * n for _ in range(n)]

    # 자기 자신으로 가는 비용 0
    for i in range(n):
        graph[i][i] = 0

    # 2) input edge data
    for _ in range(m):
        a, b = map(int, input().split())  # a -> b

        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1  # 무방향 graph 이고, 간선의 비용이 1로 고정

    # 3) Floyd_Washall 알고리즘 수행
    for k in range(n):  # 거쳐가는 지점 k
        for i in range(n):
            for j in range(m):
                graph[i][j] = min(graph[i][j], graph[i]
                                  [k] + graph[k][j])  # 점화식

    # 4) 결과 값
    for i in range(n):
        if rst[1] > sum(graph[i]):
            rst[0], rst[1] = i + 1, sum(graph[i])

    return rst[0]


# 2) bfs
def bfs_algo():
    n, m = map(int, input().split())  # node, edge

    # 1) init link graph
    links = [[False] * n for _ in range(n)]

    # 2) input edge data
    for _ in range(m):
        a, b = map(int, input().split())  # a -> b

        # 무방향 그래프
        links[a-1][b-1] = True
        links[b-1][a-1] = True

    def bfs(start):
        # 방문 노드 리스트 초기화
        visited = [False] * n
        visited[start] = True  # 시작점 방문
        dist = [0 for _ in range(n)]

        q = deque([start])

        while q:
            now = q.popleft()

            for i in range(n):
                if links[now][i]:
                    if not visited[i]:
                        q.append(i)
                        visited[i] = True
                        dist[i] = dist[now] + 1  # 현재 노드보다 1단계 더 이동한 노드

        return sum(dist)

    rst = [bfs(i) for i in range(n)]

    return rst.index(min(rst)) + 1


# print(floyd_warshall())
print(bfs_algo())


"""
1) Floyd_Warshall Algorithm
    - 모든 노드에서 모든 노드로 가는 최단거리를 구하는데 사용하는 알고리즘 삼중 for문으로 인해서 O(n^3)의
      시간 복잡도를 갖지만, 모든 노드로 가는 비용을 구한다는데 장점이 있다.
    
    - 2차원 테이블에 최단거리를 저장한다. 
    - 각 단계에서 특정 노드 k를 거쳐가는 경우를 계산한다. 
    - 다이나믹 프로그래밍 유형에 속한다. 

2) bfs를 이용한 최단거리 구하기
    - 이 문제에서 graph의 간선 간 가중치가 모두 1로 동일하다. (단순 인간관계에 대해 몇단계만에 연결되는지 봄)
      때문에 가중치가 없는 graph에서 최단거리를 구할 때, 사용할 수 있는 방법으로 bfs 알고리즘을 채택할 수 있다.
    
    - 완전탐색 기법으로 현재 node(a)에서 갈 수있는 방문하지 않은 node(b)를 방문하는 방식으로 구현이 가능하다. 
      이때, 다음 노드(b)는 이전 노드(a)의 다음 방문 노드이므로 가중치가 1로 모두 동일한 상황에서 채택이
      가능하다.

    - 단, bfs()의 경우 시작점이 명확하게 있으므로 for loop를 통해서 모든 값을 찾은 후 다시 최소 값의 index를
      구해서 답을 찾아냈다. 
"""
