# 2025.02.21 FRI
# https://www.acmicpc.net/problem/15889

import sys

input = sys.stdin.readline

N = int(input())
loc = list(map(int, input().split()))
power = list(map(int, input().split()))

mx = 0
for i in range(N - 1):
    if mx >= loc[i]:
        mx = max(mx, loc[i] + power[i])

print("권병장님, 중대장님이 찾으십니다") if mx >= loc[N - 1] else print("엄마 나 전역 늦어질 것 같아")
