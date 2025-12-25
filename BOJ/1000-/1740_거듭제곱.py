# 2024.09.18 WED
# https://www.acmicpc.net/problem/1740

import sys

input = sys.stdin.readline

N = int(input())
i = 0
ans = 0
while N:
    if N & 1:
        ans += 3**i
    N >>= 1
    i += 1
print(ans)
