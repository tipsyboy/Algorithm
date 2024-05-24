# https://www.acmicpc.net/problem/16956

"""
16956. 늑대와 양
    - 이게 정해가 맞는지는 모르겠지만 늑대 주변을 몽땅 막았다.
"""

import sys

input = sys.stdin.readline
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]

ans = 1
for i in range(R):
    for j in range(C):
        if grid[i][j] != "W":
            continue

        for d in range(4):
            nx, ny = i + directions[d][0], j + directions[d][1]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if grid[nx][ny] == "S":
                ans = 0
                break
            if grid[nx][ny] == ".":
                grid[nx][ny] = "D"

    if not ans:
        break

print(ans)
if ans:
    for i in range(R):
        print("".join(grid[i]))
