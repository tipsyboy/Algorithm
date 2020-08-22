import sys

N = int(sys.stdin.readline())

for i in range(N):
    OX = sys.stdin.readline()
    count = 0
    sum_o = 0

    for j in range(len(OX)):
        if OX[j] == "O":
            count += 1
        else:
            sum_o += ((1 + count) * count) / 2  # 등차수열 합
            count = 0

    print(int(sum_o))


# 2
# N = int(input())

# for i in range(N):
#     OX = input()
#     count = 0
#     sum_o = 0

#     for j in As:
#         if j == 'O':
#             count += 1
#         else:
#             count = 0
#         sum_o += count

#     print(sum_o)
