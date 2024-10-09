# 2024.10.04 FRI
# https://www.acmicpc.net/problem/6506

import sys

input = sys.stdin.readline

ans = []
while True:
    n, k = map(int, input().split())

    if n == 0 and k == 0:
        break

    seq = list(map(int, input().split()))

    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(n):
        dp[i][1] = 1
        for j in range(i):
            if seq[i] > seq[j]:
                for col in range(2, k + 1):
                    dp[i][col] += dp[j][col - 1]

    rst = 0
    for i in range(n):
        rst += dp[i][k]

    ans.append(rst)

print(*ans, sep="\n")
