# https://www.acmicpc.net/problem/10819

import sys
from itertools import permutations

input = sys.stdin.readline
INF = float("inf")

N = int(input())
arr = list(map(int, input().split()))

ans = -INF
for per in permutations(arr, N):
    temp = 0
    for i in range(N - 1):
        temp += abs(per[i] - per[i + 1])

    ans = max(ans, temp)
print(ans)
