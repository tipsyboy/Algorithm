# https://www.acmicpc.net/problem/3860
"""
3860. 할로윈 묘지
    - 벨만-포드
"""
import sys

input = sys.stdin.readline
INF = float("inf")
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def BF(sx: int, sy: int) -> int:
    dist = [[INF] * W for _ in range(H)]
    dist[sx][sy] = 0
    cycle = False

    for i in range(W * H):
        for x in range(H):
            for y in range(W):
                if grid[x][y] == -1 or dist[x][y] == INF:
                    continue
                if x == 0 and y == W - 1:
                    continue

                if (x, y) in HOLE:
                    nx, ny, t = HOLE[(x, y)]

                    if dist[nx][ny] > dist[x][y] + t:
                        dist[nx][ny] = dist[x][y] + t

                        if i == W * H - 1:
                            return -INF
                    continue

                for d in range(4):
                    nx, ny = x + directions[d][0], y + directions[d][1]

                    if nx < 0 or nx >= H or ny < 0 or ny >= W:
                        continue
                    if grid[nx][ny] == -1:
                        continue

                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1

                        if i == W * H - 1:
                            return -INF

    return dist[0][W - 1]


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    grid = [[0] * W for _ in range(H)]

    G = int(input())
    for _ in range(G):
        X, Y = map(int, input().split())
        grid[H - Y - 1][X] = -1

    E = int(input())
    HOLE = dict()
    for _ in range(E):
        X1, Y1, X2, Y2, T = map(int, input().split())
        HOLE[(H - Y1 - 1, X1)] = (H - Y2 - 1, X2, T)

    rst = BF(H - 1, 0)
    if rst == INF:
        print("Impossible")
    elif rst == -INF:
        print("Never")
    else:
        print(rst)

"""
4 2
0
1
2 0 1 0 -2
0 0
ans = Never

3 3
2
2 1
1 2
1
1 0 1 0 -1
0 0
ans = Never

5 3
3
1 0
1 1
3 2
2
3 0 4 1 -1
3 1 3 0 0
0 0
ans = 6

3 3
2
1 1
2 0
1
2 1 2 2 -10
0 0
ans = 4

3 3
0
1
1 1 2 1 5
0 0
ans = 4
"""