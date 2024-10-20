# 2024.10.14 MON
# https://www.acmicpc.net/problem/13301


import sys

input = sys.stdin.readline

N = int(input())

d = [1, 1, 2]
for i in range(3, N):
    d.append(d[-1] + d[-2])

print(4 * d[N - 1] + 2 * d[N - 2]) if N > 1 else print(4)
