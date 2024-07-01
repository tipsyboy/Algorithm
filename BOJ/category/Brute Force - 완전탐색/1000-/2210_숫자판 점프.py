# https://www.acmicpc.net/problem/2210

import sys

input = sys.stdin.readline


def dfs(x, y, depth, nums):
    global ans

    if depth == 6:
        ans.add("".join(nums))
        return

    nums.append(grid[x][y])

    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + i, y + j

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        dfs(nx, ny, depth + 1, nums)

    nums.pop()


grid = [list(input().split()) for _ in range(5)]
ans = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, 0, [])
print(len(ans))
