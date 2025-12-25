# 2024.08.17 SAT
# https://www.acmicpc.net/problem/15831

import sys

input = sys.stdin.readline

N, B, W = map(int, input().split())
trails = list(input().rstrip())

L, R = 0, -1
cnt = {"B": 0, "W": 0}
ans = 0
while R < N:
    if cnt["B"] > B:
        cnt[trails[L]] -= 1
        L += 1
    else:
        R += 1
        if R < N:
            cnt[trails[R]] += 1
    if R < N and cnt["W"] >= W and cnt["B"] <= B:
        ans = max(ans, R - L + 1)

print(ans)
