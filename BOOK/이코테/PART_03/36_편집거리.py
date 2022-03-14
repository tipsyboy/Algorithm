import sys

input = sys.stdin.readline


def shortest_edit(string1, string2):
    n = len(string1)
    m = len(string2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    #
    for i in range(n + 1):
        dp[i][0] = i
    for i in range(m + 1):
        dp[0][i] = i

    #
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1


    return dp[n][m]


string1 = input().rstrip()
string2 = input().rstrip()

print(shortest_edit(string1, string2))
