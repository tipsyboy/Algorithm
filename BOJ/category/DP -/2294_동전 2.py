import sys

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [[INF] * (k + 1) for _ in range(n)]
for i in range(k + 1):
    if i % coins[0] != 0:
        continue
    dp[0][i] = i // coins[0]

for i in range(1, n):
    for j in range(k + 1):
        if coins[i] <= j and dp[i][j - coins[i]] != INF:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i]] + 1)
        else:
            dp[i][j] = dp[i - 1][j]

if dp[n - 1][k] == INF:
    print(-1)
else:
    print(dp[n - 1][k])
