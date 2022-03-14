import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def DFS(now):
    # if visited[now]: # 왜 필요하지..?
    #     return dp[now]

    visited[now] = True

    for adj in graph[now]:
        if visited[adj]:
            continue
        dp[now] += DFS(adj)

    return dp[now]


N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())

    # 트리는 무방향 그래프이다.
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
dp = [1] * (N + 1)  # 정점 i를 루트로하는 서브트리의 정점 개수. 이때 정점 i를 포함하므로 1로 시작한다.
DFS(R)

for _ in range(Q):
    query = int(input())
    print(dp[query])


"""
    트리 
    - 임의의 두 노드 u, v에서 최단 경로는 유일하다.
    - 임의의 노드 x를 잡고 부모노드와의 간선을 끊으면, 서브트리가 된다. 

    - 트리에서의 정보를 DP로 저장한다 개념
"""