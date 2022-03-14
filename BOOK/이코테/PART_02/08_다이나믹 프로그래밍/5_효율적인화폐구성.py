n, k = map(int, input().split())
coin_types = []

for i in range(n):
    coin_types.append(int(input()))


dp = [10001] * (k + 1)
dp[0] = 0

for coin in coin_types:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)


print(dp)
