# 1. 더하고 빼고 - 시간초과 (16)

# import sys
# import time

# n = int(sys.stdin.readline())

# start = time.time()
# stair_num = [[] for i in range(n)]

# # 한 자릿수
# for i in range(1, 10):
#     stair_num[0].append(i)

# for i in range(1, n):
#     for num in stair_num[i-1]:
#         if i == 1:
#             units = num
#         else:
#             units = num % (10**(i-1))

#         if units == 0:
#             new_num = int(str(num) + "1")
#             stair_num[i].append(new_num)
#         elif units == 9:
#             new_num = int(str(num) + "8")
#             stair_num[i].append(new_num)
#         else:
#             new_num_one = int(str(num) + str(units-1))
#             new_num_two = int(str(num) + str(units+1))
#             stair_num[i].append(new_num_one)
#             stair_num[i].append(new_num_two)

# print(len(stair_num[i]))
# print(time.time() - start)


# 2. 개수만 세기 - 끝자리수가 j인

import sys

n = int(sys.stdin.readline())

stair_num = [[0 for i in range(10)] for j in range(n)]

for i in range(1, 10):
    stair_num[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            stair_num[i][0] = stair_num[i-1][1]
        elif j == 9:
            stair_num[i][9] = stair_num[i-1][8]
        else:
            stair_num[i][j] = stair_num[i-1][j-1]+stair_num[i-1][j+1]

print(sum(stair_num[n-1]) % 1000000000)
