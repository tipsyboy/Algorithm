# https://www.acmicpc.net/problem/10025

import sys

input = sys.stdin.readline
X_MAX = 1_000_000

N, K = map(int, input().split())
ice = [0] * (X_MAX + 1)
for _ in range(N):
    g, x = map(int, input().split())
    ice[x] = g

psum = [0]
for i in range(X_MAX + 1):
    psum.append(ice[i] + psum[-1])

ans = -1
for i in range(X_MAX):
    ans = max(ans, psum[min(X_MAX, i + K)] - psum[max(0, i - K - 1)])
print(ans)
