# https://www.acmicpc.net/problem/9501

import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, D = map(int, input().split())

    cnt = 0
    for __ in range(N):
        v, f, c = map(int, input().split())
        if D <= v * f / c:
            cnt += 1

    print(cnt)