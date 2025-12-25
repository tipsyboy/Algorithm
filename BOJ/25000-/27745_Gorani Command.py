# 2025.01.24 FRI
# https://www.acmicpc.net/problem/27445

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

rows = [int(input()) for _ in range(N - 1)]
cols = list(map(int, input().split()))
rows.append(cols[0])

r = rows.index(min(rows)) + 1
c = cols.index(min(cols)) + 1
print(r, c)
