# 2024.10.06 SUN
# https://www.acmicpc.net/problem/7571


import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pos_X, pos_Y = [], []
for _ in range(M):
    x, y = map(int, input().split())
    pos_X.append(x)
    pos_Y.append(y)

pos_X.sort()
pos_Y.sort()

mx = pos_X[M // 2]
my = pos_Y[M // 2]
ans = 0
for x, y in zip(pos_X, pos_Y):
    ans += abs(mx - x) + abs(my - y)
print(ans)
