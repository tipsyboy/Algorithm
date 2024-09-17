# 2024.09.10 TUE
# https://www.acmicpc.net/problem/5600

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
N = int(input())
ans = [2] * (a + b + c + 1)

check = []
for _ in range(N):
    i, j, k, r = map(int, input().split())

    if r == 1:
        ans[i] = ans[j] = ans[k] = 1
    else:
        check.append((i, j, k))

for i, j, k in check:
    if ans[i] == 1 and ans[j] == 1:
        ans[k] = 0
    elif ans[i] == 1 and ans[k] == 1:
        ans[j] = 0
    elif ans[j] == 1 and ans[k] == 1:
        ans[i] = 0

print(*ans[1:], sep="\n")
