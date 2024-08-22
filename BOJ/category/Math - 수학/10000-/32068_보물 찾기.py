# 2024.08.16 FRI
# https://www.acmicpc.net/problem/32068

import sys

input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    L, R, S = map(int, input().split())
    L -= S
    R -= S

    if abs(L) >= abs(R):
        minv = R
        abs_minv = abs(R)
    elif abs(L) < abs(R):
        minv = L
        abs_minv = abs(L)

    rst = (abs_minv - 1) * 2 + 1
    if minv < 0:
        rst += 1

    ans.append(rst + 1)

print(*ans, sep="\n")
