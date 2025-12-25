# 2024.10.26 SAT
# https://www.acmicpc.net/problem/31713

import sys

input = sys.stdin.readline
INF = float("inf")


T = int(input())
ans = []
for _ in range(T):
    A, B = map(int, input().split())  # A: 줄기 개수, B: 클로버 잎의 개수

    rst = 0

    while A * 4 < B:
        A += 1
        rst += 1

    if A * 3 > B:
        rst += A * 3 - B

    ans.append(rst)

print(*ans, sep="\n")
