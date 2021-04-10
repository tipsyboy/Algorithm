
# # 1) 내 풀이
# n, m = map(int, input().split())
# ball = list(map(int, input().split()))

# combination = []
# count = 0  # 조합 개수

# for i in range(len(ball)-1):
#     for j in range(i+1, len(ball)):
#         if ball[i] != ball[j]:
#             count += 1
#             combination.append((i+1, j+1))

# print(combination)
# print(count)


# # 2) 해설지 풀이
# n, m = map(int, input().split())
# ball = list(map(int, input().split()))

# weight = [0] * 11
# count = 0

# for b in ball:
#     weight[b] += 1

# for i in range(1, m+1):
#     n -= weight[i]
#     count += weight[i] * n

# print(count)
