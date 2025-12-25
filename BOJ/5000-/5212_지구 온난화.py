# https://www.acmicpc.net/problem/5212

import sys

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = float("inf")

R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]
maxi, maxj = -1, -1
mini, minj = INF, INF
island = set()
for i in range(R):
    for j in range(C):
        if grid[i][j] == ".":
            continue

        cnt = 0
        for d in range(4):
            ax, ay = i + directions[d][0], j + directions[d][1]

            if ax < 0 or ax >= R or ay < 0 or ay >= C or grid[ax][ay] == ".":
                cnt += 1

        if cnt < 3:
            island.add((i, j))

            maxi, mini = max(maxi, i), min(mini, i)
            maxj, minj = max(maxj, j), min(minj, j)

for i in range(mini, maxi + 1):
    for j in range(minj, maxj + 1):
        if (i, j) in island:
            print("X", end="")
        else:
            print(".", end="")
    print()
