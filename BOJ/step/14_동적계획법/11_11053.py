# import sys

# n = int(sys.stdin.readline())

# lst = list(map(int, sys.stdin.readline().split()))
# check_lst = [lst[0]]

# for i in range(1, n):
#     if lst[i] > check_lst[-1]:
#         # 1. 이전항에 새 값 추가하기
#         check_lst.append(lst[i])
#         print(f"{i+1}: {check_lst}")
#         continue

#     # 2. 이전항을 순회하며 값을 교체하기
#     if lst[i] in check_lst:
#         print(f"{i+1}: {check_lst}")
#         continue
#     else:
#         for j in range(len(check_lst)):
#             if check_lst[j] > lst[i]:
#                 check_lst[j] = lst[i]
#                 break
#         print(f"{i+1}: {check_lst}")

#     # 3. 아니면 이전항을 그대로 쓴다.
# print(check_lst)
# print(len(check_lst))


###

import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(n)]

for i in range(n):
    dp_max = 0
    for j in range(i):  # 현재 항 전까지의 값들중에서
        if lst[j] < lst[i]:  # 현재 항의 값보다 작은 것들 중
            dp_max = max(dp_max, dp[j])  # 가장 긴 부분수열의 길이 (LIS)

    dp[i] = dp_max + 1  # i-1까지의 LIS에 나를 추가

# print(dp)
print(max(dp))
