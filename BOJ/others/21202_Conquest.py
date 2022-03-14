import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution(start):
    visited = [False] * (n + 1)
    visited[start] = True
    pq = []
    now_power = power[start - 1]

    for adj in graph[start]:
        heappush(pq, (power[adj - 1], adj))
        visited[adj] = True

    while pq:
        p, node = heappop(pq)

        if now_power <= p:
            break

        now_power += p

        for adj in graph[node]:
            if not visited[adj]:
                heappush(pq, (power[adj - 1], adj))
                visited[adj] = True

    return now_power


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

power = []
for _ in range(n):
    power.append(int(input()))

print(solution(1))
