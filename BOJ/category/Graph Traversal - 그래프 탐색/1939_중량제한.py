import sys
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e10)


def solution1() -> int:
    # 1) 그래프 탐색 + 이분 탐색
    def bfs(start, end, target) -> bool:
        q = deque()
        visited = [False] * (N + 1)
        q.append(start)
        visited[start] = True

        while q:
            now = q.popleft()

            for adj_node, adj_cost in graph[now]:
                if visited[adj_node] or adj_cost < target:
                    continue

                if adj_node == end:
                    return True

                q.append(adj_node)
                visited[adj_node] = True

        return False

    def binary_search(start, end, lo, hi) -> int:
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if bfs(start, end, mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans

    # main
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    lo, hi = INF, 1
    for _ in range(M):
        A, B, C = map(int, input().split())
        lo = min(lo, C)
        hi = max(hi, C)
        graph[A].append((B, C))
        graph[B].append((A, C))
    start, end = map(int, input().split())

    return binary_search(start, end, lo, hi)


def solution2() -> int:
    # 2. 유니온-파인드 이용
    def union_parent(a, b):
        a, b = find_parent(a), find_parent(b)

        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])

        return parent[x]

    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        A, B, C = map(int, input().split())
        heappush(edges, (-C, A, B))
    start, end = map(int, input().split())

    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        parent[i] = i

    while edges:
        C, A, B = heappop(edges)
        C *= -1

        union_parent(A, B)
        if find_parent(start) == find_parent(end):
            return C


def solution3() -> int:
    # 3. 다익스트라 알고리즘 이용
    def search(start, end) -> int:
        pq = []
        heappush(pq, (-INF, start))
        dist = [-1] * (N + 1)
        dist[start] = INF

        while pq:
            now_cost, now_node = heappop(pq)
            now_cost *= -1

            if now_cost < dist[now_node]:
                continue

            for adj_node, adj_cost in graph[now_node]:
                cost = min(now_cost, adj_cost)
                if cost > dist[adj_node]:
                    dist[adj_node] = cost
                    heappush(pq, (-cost, adj_node))

        return dist[end]

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
    start, end = map(int, input().split())

    return search(start, end)


# print(solution1())
# print(solution2())
print(solution3())


"""
1939. 중량제한
    - 간단해 보였지만 꽤나 해맸음
    
    - 처음에는 BFS + 이분 탐색으로 해결했고, 이후에 3가지 풀이가 있다고 해서 찾아서 전부 확인했다. 
    - 유니온 파인드 방식으로 푼게 가장 간단한 풀이인듯.
"""