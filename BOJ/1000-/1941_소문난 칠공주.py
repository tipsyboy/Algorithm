# https://www.acmicpc.net/problem/1941

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check_the_group(pos: tuple) -> bool:
    cnt_y = 0
    for p in pos:
        x, y = p // 5, p % 5
        if grid[x][y] == "Y":
            cnt_y += 1

    return cnt_y < 4


def check_the_pos(pos: tuple) -> bool:
    if not check_the_group(pos):
        return False

    sx, sy = pos[0] // 5, pos[0] % 5
    q = deque([(sx, sy)])
    visited = set()
    visited.add(pos[0])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if nx * 5 + ny not in pos or nx * 5 + ny in visited:
                continue

            q.append((nx, ny))
            visited.add(nx * 5 + ny)

    return len(visited) == 7


grid = [list(input().rstrip()) for _ in range(5)]
ans = 0
for pos in combinations(range(0, 25), 7):
    if check_the_pos(pos):
        ans += 1

print(ans)