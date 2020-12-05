# # 1. 처음 풀이 - 틀렸음
# import sys

# n = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))

# dp = [0 for i in range(n)]
# dp_rvs = [0 for i in range(n)]

# for i in range(n):
#     dp_max = 0
#     for j in range(i):
#         if lst[i] > lst[j]:
#             dp_max = max(dp_max, dp[j])

#     dp[i] = dp_max + 1

# for i in range(n-1, -1, -1):
#     dp_max = 0
#     for j in range(n-1, i, -1):
#         if lst[i] > lst[j]:
#             dp_max = max(dp_max, dp_rvs[j])

#     dp_rvs[i] = dp_max + 1

# dp_idx = dp.index(max(dp))
# dp_rvs_idx = dp_rvs.index(max(dp_rvs))

# ans = max(dp[dp_idx] + dp_rvs[dp_idx], dp[dp_rvs_idx] + dp_rvs[dp_rvs_idx]) - 1

# print(f"[dp]: {dp}")
# print(f"[dp_rvs]: {dp_rvs}")
# print(f"[dp_idx]: {dp_idx}")
# print(f"[dp_rvs_idx]: {dp_rvs_idx}")
# print(ans)


# 2. 정답풀이

import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(n)]
dp_rvs = [0 for i in range(n)]
rst = [0 for i in range(n)]

for i in range(n):
    dp_max = 0
    for j in range(i):
        if lst[i] > lst[j]:
            dp_max = max(dp_max, dp[j])

    dp[i] = dp_max + 1

for i in range(n-1, -1, -1):
    dp_max = 0
    for j in range(n-1, i, -1):
        if lst[i] > lst[j]:
            dp_max = max(dp_max, dp_rvs[j])

    dp_rvs[i] = dp_max + 1

# print(dp)
# print(dp_rvs)

for i in range(n):
    rst[i] = dp[i] + dp_rvs[i] - 1

# print(rst)
print(max(rst))
