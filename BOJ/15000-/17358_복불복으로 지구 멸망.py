# 2024.07.03 WED
# https://www.acmicpc.net/problem/17358

import sys

input = sys.stdin.readline
DIV = 1_000_000_000 + 7

N = int(input())
ans = 1
for i in range(N - 1, 0, -2):
    ans = (ans * i) % DIV
print(ans)
