import sys

input = sys.stdin.readline
dy = [-1, 0, 1, 0]  # 상 우 하 좌 순
dx = [0, 1, 0, -1]
direction = {1: (1,), 2: (1, 3), 3: (0, 1), 4: (0, 1, 3), 5: (0, 1, 2, 3)}


def check_map(status):
    checked = set()

    for i in range(len(cctv_pos)):
        cctv_type = cctv_pos[i][0]
        y = cctv_pos[i][1]
        x = cctv_pos[i][2]

        checked.add((y, x))  # cctv 위치

        for d in direction[cctv_type]:
            idx = 1
            while True:
                ny = y + dy[(d + status[i]) % 4] * idx
                nx = x + dx[(d + status[i]) % 4] * idx
                idx += 1

                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    break

                if graph[ny][nx] == 6:
                    break

                if (ny, nx) in checked:
                    continue

                checked.add((ny, nx))

    return candidate_pos - len(checked)


def dfs(picked, status):
    global rst

    if picked == len(cctv_pos):
        rst = min(rst, check_map(status))
        return

    for i in range(4):
        status.append(i)
        dfs(picked + 1, status)
        status.pop()


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
rst = int(1e9)

cctv_pos = []
wall_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 and graph[i][j] < 6:
            cctv_pos.append((graph[i][j], i, j))  # cctv종류, 좌표

        if graph[i][j] == 6:
            wall_cnt += 1

candidate_pos = n * m - wall_cnt
dfs(0, [])

print(rst)
