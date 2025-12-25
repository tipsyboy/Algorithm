# 2024.09.25 WED
# https://www.acmicpc.net/problem/21610

# 격자의 숫자는 바구니에 담겨있는 물의 양이다.
# 구름의 이동에서는 맵이 연결되어있음.
# 이동 명령 이후의 동작
# 0. (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
# 1. 구름의 이동
# 2. 각각의 구름에서 비가 내려서 바구니의 물의 양이 1씩 증가
# 3. 구름이 모두 사라진다.
# 4. 물복사 버그 시전. 물복사버그 - 대각방향의 물이 있는 바구니의 수만큼 바구니의 물의 양이 증가한다. 이동과는 다르게 대각은 맵이 연결되어있지 않다.
# 5. 바구니 물 >= 2, 모든 칸에 구름 생성. 구름 사라진 칸은 안생김.

import sys

input = sys.stdin.readline
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def move_cloud(cloud, d, s):
    nxt = []
    for x, y in cloud:
        nx, ny = (x + directions[d][0] * s) % N, (y + directions[d][1] * s) % N

        nxt.append((nx, ny))

    return nxt


def add_water(cloud):
    for x, y in cloud:
        grid[x][y] += 1


def copy_water_bug(cloud):
    for x, y in cloud:
        cnt = 0
        for d in [1, 3, 5, 7]:
            nx, ny = x + directions[d][0], y + directions[d][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if grid[nx][ny]:
                cnt += 1

        grid[x][y] += cnt


def create_new_cloud(cloud):
    new_cloud = []

    for i in range(N):
        for j in range(N):
            if grid[i][j] >= 2 and (i, j) not in cloud:
                grid[i][j] -= 2
                new_cloud.append((i, j))

    return new_cloud


def solution(N, M, grid):
    cloud = [(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)]

    for _ in range(M):
        d, s = map(int, input().split())

        moved_cloud = move_cloud(cloud, d - 1, s)
        add_water(moved_cloud)
        copy_water_bug(moved_cloud)
        new_cloud = create_new_cloud(set(moved_cloud))
        cloud = new_cloud

    ans = 0
    for i in range(N):
        for j in range(N):
            ans += grid[i][j]

    return ans


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, M, grid))
