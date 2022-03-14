from collections import deque


n, left, right = map(int, input().split())
graph = []  # map data
rst = 0  # 인구 이동 횟수

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y):
    # 출발 지점 (x, y) 세팅
    united = [(x, y)]  # 분배를 위한 방문 국가 저장
    q = deque([(x, y)])  # bfs를 위해서 queue 생성
    visited[x][y] = True  # 현재 국가를 방문함
    sum_value = graph[x][y]  # 국가 인구수
    count = 1  # 방문한 국가 수

    while q:
        now_x, now_y = q.popleft()

        # 4방향 탐색
        for i in range(4):
            nx = now_x + dx[i]  # 다음 좌표
            ny = now_y + dy[i]

            # 갈 수 있는 곳인지 판단
            if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny]:
                if left <= abs(graph[nx][ny] - graph[now_x][now_y]) <= right:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    sum_value += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    temp = int(sum_value / count)
    for x, y in united:
        graph[x][y] = temp


# 1. 더 이상 인구이동이 없을 때까지
while True:
    visited = [[False] * n for _ in range(n)]
    index = 0

    # 2. 첫 원소부터 돌면서 방문
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:  # 방문하지 않은 국가
                move(i, j)
                index += 1  # 모든 원소를 전부 탐색할 때까지 돌려야 하기 때문에 index 추가

    # 모든 원소를 전부 탐색했을 때 - 더이상 국경을 열 곳이 없다.
    if index == n * n:
        print(graph)
        break

    rst += 1

print(rst)
