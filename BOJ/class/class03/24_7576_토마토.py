"""
23(7569)번 토마토의 더 쉬운 버전 등급이 같은데 이 문제가 번호가 높아서 
solved 에서는 나중에 나왔다. 순서가 엉망이다 ㅠ
"""

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    # 좌표 이동
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        x, y = q.popleft()  # 행 렬

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    q.append((nx, ny))
                    box[nx][ny] = box[x][y] + 1


def check_box():
    max_value = 0

    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:  # bfs()를 수행 후에 안 익은 토마토가 있다.
                return -1
            max_value = max(max_value, box[i][j])

    return max_value - 1


m, n = map(int, input().split())  # 열, 행

box = list(list(map(int, input().split())) for _ in range(n))

q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))


bfs()
# print(box)
print(check_box())
