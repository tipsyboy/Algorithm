# 2024.11.13. WED
# https://www.acmicpc.net/problem/19621

# `임의의 회의 K(1≤ K ≤ N)는 회의 K − 1과 회의 K + 1과는 회의 시간이 겹치고 다른 회의들과는 회의 시간이 겹치지 않는다.`

import sys

input = sys.stdin.readline

N = int(input())
d = [0] * (N + 1)
for i in range(1, N + 1):
    s, e, x = map(int, input().split())
    d[i] = max(d[i - 1], d[i - 2] + x)

print(d[-1])
