from collections import deque

n, m, k, x = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(n + 1)]

# 간선 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 도시간 거리 최소화
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 지점 거리

q = deque([x])  # 출발 지점 초기화

while q:
    now = q.popleft()  # 현재 위치

    for next_node in graph[now]:
        # 미 방문 도시인 경우
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 거리 계산 이후에
flag = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)
