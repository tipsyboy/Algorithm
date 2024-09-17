# 2024.09.13 FRI
# https://www.acmicpc.net/problem/4312

import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    n -= 1
    ans = []
    i = 0
    while n:
        if n & 1:
            ans.append(3**i)
        n >>= 1
        i += 1

    if ans:
        print("{", ", ".join(map(str, ans)), "}")
    else:
        print("{ }")
