def solution(n, arr):
    target = arr[n - 1]

    dp = [[0] * 21 for _ in range(n - 1)]
    dp[0][arr[0]] = 1
    for i in range(1, n - 1):
        now = arr[i]
        for j in range(21):
            if dp[i - 1][j] == 0:
                continue
            if 0 <= j - now < 21:
                dp[i][j - now] += dp[i - 1][j]
            if 0 <= j + now < 21:
                dp[i][j + now] += dp[i - 1][j]

    # print(*dp, sep="\n")
    return dp[n - 2][target]


n = int(input())
arr = list(map(int, input().split()))

print(solution(n, arr))

"""
5557. 1학년 (Gold 5)
    -
    -    
"""
