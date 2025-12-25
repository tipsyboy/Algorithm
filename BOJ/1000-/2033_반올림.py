# https://www.acmicpc.net/problem/2033

import sys

input = sys.stdin.readline

N = int(input())
d = 1
while N > 10:
    if N % 10 >= 5:
        N = N // 10 + 1
    else:
        N //= 10
    d *= 10
print(N * d)