import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    # input data
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    # 2차원 배열로 옮기기
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j] = arr[m * i + j]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j - 1]) + dp[i][j]
            elif i == n - 1:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1]) + dp[i][j]
            else:
                dp[i][j] = (
                    max(dp[i][j - 1], dp[i - 1][j - 1], dp[i + 1][j - 1]) + dp[i][j]
                )

    rst = 0
    for i in range(n):
        rst = max(rst, dp[i][m - 1])

    print(rst)

"""
# test case

2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""