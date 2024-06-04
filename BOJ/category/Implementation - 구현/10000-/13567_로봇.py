# https://www.acmicpc.net/problem/13567

import sys

input = sys.stdin.readline
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


M, n = map(int, input().split())
x, y = 0, 0
to = 0
flag = False
for _ in range(n):
    command, d = input().split()

    if command == "TURN":
        if d == "0":
            to = (to - 1) % 4
        elif d == "1":
            to = (to + 1) % 4
    elif command == "MOVE":
        nx, ny = x + directions[to][0] * int(d), y + directions[to][1] * int(d)

        if nx < 0 or nx > M or ny < 0 or ny > M:
            flag = True
            break

        x, y = nx, ny

print(-1) if flag else print(x, y)
