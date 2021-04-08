import sys

#
input = sys.stdin.readline  # 입력 속도를 빠르게 하기 위해서 sys.stdin.readline를 input으로 치환
INF = int(1e9)  # 무한을 의미하는 값 10억 설정

#
n, m = map(int, input().split())  # n 노드 수, m 간선 수
start = int(input())  # 시작 노드 입력

#
graph = [[] for i in range(n + 1)]  # 노드 그래프
visited = [False] * (n + 1)  # 방문 노드
distance = [INF] * (n + 1)

# graph 입력 받기
for i in range(m):
    a, b, c = map(int, input().split())  # a노드에서 b로 가는 비용이 c
    graph[a].append((b, c))


# 현재 노드상황에서 최단 거리를 가진 노드를 얻는 함수
def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1, n + 1):
        if not visited[i] and (distance[i] < min_value):
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    # start Node에 대한 처리
    visited[start] = True
    distance[start] = 0
    for i in graph[start]:
        distance[i[0]] = i[1]  # start 노드에 연결된 노드들의 dist를 추가

    # 시작 노드를 제외한 모든 노드에 대해서 순회한다.
    for i in range(n - 1):
        now = get_smallest_node()  # 현재 노드에서 가장 가까운 노드로 이동
        visited[now] = True  # 방문 확인

        for j in graph[now]:
            # cost = distance[now] + j[1]
            # if cost < distance[j[0]]:
            #     distance[j[0]] = cost
            cost = min(distance[j[0]], distance[now] + j[1])  # 원래dist와 현재 노드를 거쳐가는 값 비교
            distance[j[0]] = cost


dijkstra(start)  #

print(distance)
