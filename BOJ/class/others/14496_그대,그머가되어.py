import sys
from heapq import heappush, heappop
from collections import deque

input = sys.stdin.readline
INF = int(1e9)


# 1.
def dijkstra(start, end):
    pq = []
    dist = [INF] * (n + 1)
    dist[start] = 0
    heappush(pq, (0, start))

    while pq:
        now_cost, now_node = heappop(pq)

        if now_node == end:
            break

        if dist[now_node] < now_cost:
            continue

        for adj_node in graph[now_node]:
            if dist[now_node] + 1 < dist[adj_node]:
                dist[adj_node] = dist[now_node] + 1
                heappush(pq, (dist[now_node] + 1, adj_node))

    if dist[end] == INF:
        return -1

    return dist[end]


# 2.
def bfs1(start, end):
    q = deque([(start, 0)])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        now, cost = q.popleft()
        if now == end:
            return cost

        for nxt in graph[now]:
            if not visited[nxt]:
                q.append((nxt, cost + 1))
                visited[nxt] = True

    return -1


def bfs2(start, end):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    time = 0

    while q:
        length = len(q)

        for _ in range(length):
            now = q.popleft()

            if now == end:
                return time

            for nxt in graph[now]:
                if not visited[nxt]:
                    q.append(nxt)
                    visited[nxt] = True

        time += 1

    return -1


start, end = map(int, input().split())  # 바꾸려는 문자 start -> end
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

# # 1.
# print(dijkstra(start, end))

# # 2.
# print(bfs1(start, end))

# 3.
print(bfs2(start, end))