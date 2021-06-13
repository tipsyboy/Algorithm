import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node):
    visited[node] = True  # 현재 노드 방문 처리

    # 현재 노드의 인접 노드(adjacent node)들을 순회하면서
    for adj_node in graph[node]:
        if not visited[adj_node]:  # 방문 하지 않은 노드면
            # 현재 노드가 인접 노드의 부모노드가 된다. (-1 했으므로 +1로 저장)
            rst[adj_node] = node + 1
            dfs(adj_node)  # 이제 인접노드로 다시 dfs()를 호출한다.


def bfs(start):
    visited = [False] * n  # 방문 리스트
    rst = [0] * n  # 결과 저장 리스트
    q = deque([start])  # 시작 노드 que에 추가

    while q:
        now = q.popleft()  # 현재 노드를 꺼낸후

        # 인접 노드를 확인한다.
        for adj_node in graph[now]:
            if not visited[adj_node]:  # 방문하지 않았으면
                rst[adj_node] = now + 1  # 결과를 저장하고
                q.append(adj_node)  # que에 추가한 뒤
                visited[adj_node] = True  # 방문 처리한다.

    return rst  # 결과 값 return


n = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n  # node 방문 check
rst = [0] * n  # 결과 저장

# 트리 입력 - n-1개의 간선
for _ in range(n-1):
    a, b = map(int, input().split())

    # tree 구조로 무방향 그래프, 1번노드를 0번노드로 사용하기 때문에 -1
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# # 1) dfs
# dfs(0)
# print("\n".join(map(str, rst[1:])))  # dfs 출력

# 2) bfs
print("\n".join(map(str, bfs(0)[1:])))


"""
06. 11725 트리의 부모 찾기 (Silver 2)
    - 모든 노드의 부모 노드를 찾아야 하므로, (1번은 루트로 사용) 완전 탐색 문제에 해당한다.
      따라서 graph이론을 알고 있어야 하며, graph 탐색에 해당한다. 
      완전 탐색을 위해서는 일단 dfs/bfs를 떠올려야 한다. 
    
    - dfs() - 첫 시도
      처음에 계속 런타임 오류 때문에 오답처리를 받아서 setrecursionlimit()를 해줬는데도, 
      런타임 오류가 떠서 해멨다. 근데 100만까지 늘려주니까 되더라.. 
      노드의 개수가 10만까지라서 10**5 까지만 늘려줬던게 문제가 되었던것 같다. 
      그 외에는 잠깐만 생각하면 거의 전형적인 dfs 문제라서 어려움은 없었던 것 같다. 

    - bfs()
      특별한거 없음

    - 출력 부분에서 0번(1번노드)는 출력하지 않기 때문에 슬라이싱으로 진행했다
"""
