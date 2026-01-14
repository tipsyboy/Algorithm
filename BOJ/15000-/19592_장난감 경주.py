# 2025.03.30 Sun
# https://www.acmicpc.net/problem/19592

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    V = list(map(int, input().split()))

    winner = float("inf")
    for i in range(N - 1):
        winner = min(winner, X / V[i])

    if X / V[N - 1] < winner:
        print(0)
        continue

    lo, hi = 0, Y
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        t = ((X - mid) / V[N - 1]) + 1
        if t < winner:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)
