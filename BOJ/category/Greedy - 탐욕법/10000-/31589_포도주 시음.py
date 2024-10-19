# 2024.10.13 SUN
# https://www.acmicpc.net/problem/31589

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
T = list(map(int, input().split()))

T.sort()
lo, hi = 0, N - 1
prev, ans = 0, 0
for i in range(K):
    if i & 1:
        prev = T[lo]
        lo += 1
    else:
        ans += T[hi] - prev
        # prev = T[hi]
        hi -= 1

print(ans)
