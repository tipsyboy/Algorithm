# 2025.02.28 FRI
# https://www.acmicpc.net/problem/1421

import sys

input = sys.stdin.readline

N, C, W = map(int, input().split())
trees = []
for _ in range(N):
    trees.append(int(input()))

mx = max(trees)
ans = 0
for length in range(1, mx + 1):
    total = 0
    for tree in trees:
        cnt = tree // length
        cut = cnt if tree % length else cnt - 1

        income = cnt * length * W - cut * C
        if income > 0:
            total += income
    ans = max(ans, total)
print(ans)
