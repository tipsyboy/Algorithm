# Dec 29, Mon 2025
# https://www.acmicpc.net/problem/3474

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    x = 5
    rst = 0
    while x <= N:
        rst += N // x
        x *= 5

    print(rst)
