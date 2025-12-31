# Dec 31, Wed 2025
# https://www.acmicpc.net/problem/24578

import sys

input = sys.stdin.readline

time = input().rstrip()

ans = [[" "] * 5 for _ in range(4)]
for col in range(4):
    bit = int(time[col])

    out_col = col if col < 2 else col + 1

    for row in range(4):
        ans[3 - row][out_col] = "*" if bit & 1 else "."
        bit >>= 1
for i in range(4):
    print(*ans[i])
