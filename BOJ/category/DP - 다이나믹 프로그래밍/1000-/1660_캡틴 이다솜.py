# 2025.01.29 WED
# https://www.acmicpc.net/problem/1660

import sys

input = sys.stdin.readline
INF = 3 * (10**5) + 1

N = int(input())
needs = [1]
x = 2
while needs[-1] < N:
    needs.append(needs[-1] + x * (x + 1) // 2)
    x += 1

dp = [INF] * (N + 1)
dp[0] = 0
dp[1] = 1
for i in range(1, N + 1):
    for nd in needs:
        if nd > i:
            break
        dp[i] = min(dp[i], dp[i - nd] + 1)
print(dp)
print(dp[N])
