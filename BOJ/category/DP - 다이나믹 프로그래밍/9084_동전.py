import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N = int(input())
    coins = list(map(int, input().split()))  # 오름차순
    target = int(input())  # 최종 타깃 돈
    dp = [[0] * (target + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(target + 1):  # now target money
            if j >= coins[i - 1]:
                dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[N][target])

"""
9084. 동전 
    - 기본적 냅색 문제?
"""