# 2024.09.14 SAT
# https://www.acmicpc.net/problem/2676

import sys

input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    n, m = map(int, input().split())

    ans.append((n - m) * m + 1)
print(*ans, sep="\n")
