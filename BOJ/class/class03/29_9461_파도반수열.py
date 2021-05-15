t = int(input())  # test case

dp = [1, 1, 1, 2, 2]  # for dp memoization

for _ in range(t):
    n = int(input())

    if len(dp) < n:
        for i in range(len(dp), n):
            dp.append(dp[i-1] + dp[i-5])

    print(dp[n-1])
