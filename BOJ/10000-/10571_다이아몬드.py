# 2024.07.07 SUN
# https://www.acmicpc.net/problem/10571

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dimonds = []
    for __ in range(N):
        w, c = map(float, input().split())
        dimonds.append((w, c))

    l = [1] * N
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if dimonds[j][0] < dimonds[i][0] and dimonds[j][1] > dimonds[i][1]:
                l[i] = max(l[i], l[j] + 1)

    print(max(l))
