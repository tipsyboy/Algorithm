import sys
from collections import deque  # for bfs
input = sys.stdin.readline


def bfs():
    # 좌표 이동
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while q:
        x, y, z = q.popleft()  # 층, 행, 열 순서로 뽑기

        # 상, 하, 좌, 우, 위, 아래 6방향
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if box[nx][ny][nz] == 0:
                    q.append((nx, ny, nz))  # 방문
                    box[nx][ny][nz] = box[x][y][z] + 1


def check_box():
    max_value = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return -1
                max_value = max(max_value, box[i][j][k])

    return max_value - 1


m, n, h = map(int, input().split())  # 열, 행, 상자 높이 - 상자의 가로, 세로, 높이

box = []  # 상자 탑
for _ in range(h):
    temp = list(list(map(int, input().split())) for _ in range(n))
    box.append(temp)

# 이미 익은 토마토의 좌표를 queue에 넣기
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:  # [층, 행, 열] 위치의 토마토가 있는 경우 == 1
                q.append((i, j, k))  # 토마토의 위치를 q에 저장 for bfs


bfs()
# print(box)
print(check_box())


"""
34번 토마토에 3차원 버전
축이 하나 늘어난 만큼만 신경써주면 된다.
solved에서 레벨 정렬을 하면 이 문제가 먼저 나와서 먼저 풀게됨..  
"""