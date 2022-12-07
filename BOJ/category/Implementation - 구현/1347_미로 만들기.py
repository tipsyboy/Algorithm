# https://www.acmicpc.net/problem/1347

import sys

input = sys.stdin.readline
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def change_dir(d: int, com: str):
    if com == "L":
        d = (d - 1) % 4
    elif com == "R":
        d = (d + 1) % 4

    return d


N = int(input())
commands = input().rstrip()
d = 0
coords = [(0, 0)]
x, y = 0, 0
minx, miny, maxx, maxy = 0, 0, 0, 0

for command in commands:
    if command != "F":
        d = change_dir(d, command)
        continue

    nx, ny = x + directions[d][0], y + directions[d][1]
    minx, miny, maxx, maxy = min(minx, nx), min(miny, ny), max(maxx, nx), max(maxy, ny)
    coords.append((nx, ny))
    x, y = nx, ny

grid = [["#"] * (maxy - miny + 1) for _ in range(maxx - minx + 1)]
for x, y in coords:
    x, y = x - minx, y - miny
    grid[x][y] = "."

for i in range(maxx - minx + 1):
    print("".join(grid[i]))


"""
최소 좌표를 (0, 0)으로 가져오는
좌표 변경 아이디어
"""