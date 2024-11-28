# 2024.11.11 MON
# https://www.acmicpc.net/problem/1652

import sys

input = sys.stdin.readline

N = int(input())
room = [input().rstrip() for _ in range(N)]

row = 0
for i in range(N):
    for r in room[i].split("X"):
        if ".." in r:
            row += 1


col_room = list(zip(*room))
col = 0
for i in range(N):
    for c in "".join(col_room[i]).split("X"):
        if ".." in c:
            col += 1

print(row, col)
