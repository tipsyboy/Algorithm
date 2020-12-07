

# ### 1. 메모리 초과 (다 더함)
# import sys

# n = int(sys.stdin.readline())

# lst = list(map(int, sys.stdin.readline().split()))
# rst = []  # 결과 맵


# for i in range(n):
#     temp_rst = []
#     temp = 0

#     for j in range(i, n):
#         temp += lst[j]
#         temp_rst.append(temp)

#     rst.append(temp_rst)


# max_rst = max(rst[0])
# for i in range(1, n):
#     max_rst = max(max(rst[i]), max_rst)

# print(max_rst)


# 2.
# import sys

# n = int(sys.stdin.readline())
# num_lst = list(map(int, sys.stdin.readline().split()))
# dp = [0 for i in range(n)]  # <n항까지의 합> 과 <현재 값> 중에서 큰 값

# dp[0] = num_lst[0]

# for i in range(1, n):
#     dp[i] = max(dp[i-1] + num_lst[i], num_lst[i])

# # print(dp)
# print(max(dp))


import sys

n = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(n)]

dp[0] = num_lst[0]
result_max = -1001

for i in range(1, n):
    # 1. 현재  i항을 쓰는 값 중 큰 값
    dp[i] = max(num_lst[i], dp[i-1] + num_lst[i])

    # 2. 현재 i항을 쓰는 값 중 큰 값 vs 현재 i항을 안쓰는 값
    result_max = max(dp[i-1], dp[i])

print(result_max)
