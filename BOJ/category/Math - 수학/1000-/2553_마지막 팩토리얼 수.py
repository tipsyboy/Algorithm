# 2024.10.26 SAT
# https://www.acmicpc.net/problem/2553

import sys

input = sys.stdin.readline
DIV = 1_000_000

N = int(input())
ans = 1
for i in range(1, N + 1):
    num = i
    cnt = 0
    while num % 5 == 0:
        num //= 5
        cnt += 1

    ans *= num
    ans //= 2**cnt
    ans %= DIV


print(ans % 10)
