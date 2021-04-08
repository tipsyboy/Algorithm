import sys
import heapq

#
input = sys.stdin.readline  # 치환
INF = int(1e9)  # 무한

#
n, m = map(int, input().split())  # 노드 / 간선 입력
start = int(input())  # 최단거리 시작노드

graph = [[] for i in range(n + 1)]  # 그래프
distance = [INF] * (n + 1)  # 최단거리 테이블

# 간선 정보 입력
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a번 노드에서 b노드까지 가는 비용이 c다


def dijkstra(start):
    q = []  # 최단거리를 찾아 내기 위한 힙큐 - 파이썬 최소힙 기반

    # 시작 노드 처리
    heapq.heappush(q, (0, start))  # q list에 (거리, 노드번호)를 추가한다.
    distance[start] = 0

    # 큐가 비어있지 않다면
    while q:
        # q list의 가장 최단거리의 노드를 꺼냄
        dist, now = heapq.heappop(q)

        #
        if distance[now] < dist:
            continue

        #
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
print(distance)
