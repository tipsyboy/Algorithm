# 2024.09.22 SUN
# https://www.acmicpc.net/problem/17174

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ans = 0
while N:
    ans += N
    N = N // M

print(ans)
