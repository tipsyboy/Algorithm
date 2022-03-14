from collections import deque


n, k = map(int, input().split())  # n*n 맵, k 바이러스 개수
map_data = []  # 맵 데이터
virus_list = []  # 바이러스의 종류, 지나간 시간, 좌표 저장

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# map data / virus_list 입력 받기
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        if temp[j] != 0:
            virus_list.append((temp[j], 0, i, j))  # (바이러스 종류, 지나간 시간, x, y)

    map_data.append(temp)

# 타깃 시간과 좌표를 입력받음
target_sec, target_x, target_y = map(int, input().split())

# 낮은 순서대로 바이러스가 먼저 경쟁적으로 퍼지기 때문에 virus 오름차순으로 정렬
virus_list.sort()
q = deque(virus_list)  # 정렬한 바이러스 리스트로 queue 생성

# bfs 진행
while q:
    virus, sec, x, y = q.popleft()  # 이번에 탐색할 바이러스

    # 시간이 다 됐으면 종료
    if sec == target_sec:
        break

    # 시간이 다 안됐으면 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 맵을 벗어나는 범위 탐색 x
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if map_data[nx][ny] == 0:  # 이미 다른 바이러스가 퍼진 곳은 탐색 x
                map_data[nx][ny] = virus  # 빈 곳은 바이러스 퍼지고
                # 새로 바이러스가 퍼진 위치를 q에 추가 시간은 1초 지났으므로 sec + 1
                q.append((virus, sec + 1, nx, ny))

print(map_data[target_x - 1][target_y - 1])
