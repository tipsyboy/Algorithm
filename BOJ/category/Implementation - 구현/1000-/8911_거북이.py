# https://www.acmicpc.net/problem/8911

import sys

input = sys.stdin.readline
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

T = int(input())
for _ in range(T):
    command = input().rstrip()

    d, x, y = 0, 0, 0  # 방향, (x, y)
    minX, maxX = 0, 0
    minY, maxY = 0, 0
    for com in command:
        if com == "F":
            x, y = x + directions[d][0], y + directions[d][1]
        elif com == "B":
            x, y = x - directions[d][0], y - directions[d][1]
        elif com == "R":
            d = (d + 1) % 4
        elif com == "L":
            d = (d - 1) % 4

        if minX > x:
            minX = x
        if maxX < x:
            maxX = x
        if minY > y:
            minY = y
        if maxY < y:
            maxY = y

    # print(minX, maxX, abs(maxX - minX))
    # print(minY, maxY, abs(maxY - minY))
    print(abs(maxX - minX) * abs(maxY - minY))
