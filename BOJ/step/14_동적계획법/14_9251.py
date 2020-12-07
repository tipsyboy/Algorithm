
string_A = input()
string_B = input()

a_len = len(string_A)
b_len = len(string_B)

dp = [[0] * (b_len + 1) for i in range(a_len + 1)]

for i in range(1, a_len+1):
    for j in range(1, b_len+1):
        if string_A[i-1] == string_B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])


# string_A = input()
# string_B = input()

# alen = len(string_A)
# blen = len(string_B)

# dp = [[0] * (alen + 1) for i in range(blen + 1)]

# for i in range(1, alen+1):
#     for j in range(1, blen+1):
#         print(i, j)
#         if string_A[i-1] == string_B[j-1]:
#             dp[j][i] = dp[j-1][i-1] + 1
#         else:
#             dp[j][i] = max(dp[j][i-1], dp[j-1][i])

# print(dp)
