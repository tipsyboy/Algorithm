import sys

# 입력
n, k = map(int, sys.stdin.readline().split())
items = []

# 배낭 물품 입력
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    items.append([w, v])

# items = sorted(items, key=lambda x: x[0])  # 정렬

# 2차원 배열 dp - 행: 가져갈수 있는 개수, n번째 아이템까지 / 열: 최대 무게
# 0의 경우를 생각해서 +1씩 해준다.
dp = [[0]*(k+1) for i in range(n+1)]

#
for i in range(1, n+1):
    # i-1번째 아이템
    weight = items[i-1][0]
    value = items[i-1][1]
    for j in range(1, k+1):
        # 이번 아이템의 무게가 이번에 가져갈 수 있는 최대무게(j)보다 크면 -> 이번 아이템을 가져갈 수 없으면
        if j < weight:
            dp[i][j] = dp[i-1][j]  # 이전 개수의 이번 최대무게
        # 아니면 -> 이번 아이템을 가져갈 수 있으면
        else:  # `이번 아이템의 가치 + 이번아이템의 무게를 뺀 최대 가치` 와 이번 아이템을 안들고갈때 최대중 큰 값 선택
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

# print(dp)
print(dp[-1][-1])


####


# n, k = map(int, sys.stdin.readline().split())
# items = []

# for i in range(n):
#     w, v = map(int, sys.stdin.readline().split())
#     items.append([w, v])

# dp = dict()
# dp[0] = 0

# for now_w, now_v in items:
#     temp = []
#     for dp_w, dp_v in dp.items():
#         if now_w + dp_w <= k:
#             temp.append((now_w + dp_w, now_v + dp_v))

#     for temp_w, temp_v in temp:
#         if temp_w in dp:
#             if dp[temp_w] < temp_v:
#                 dp[temp_w] = temp_v
#         else:
#             dp[temp_w] = temp_v


# print(max(dp.values()))
