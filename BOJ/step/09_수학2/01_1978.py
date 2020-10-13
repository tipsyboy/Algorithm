# 2번
import sys


def isPrime_nubmer(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


N = int(sys.stdin.readline())

input_num = list(map(int, sys.stdin.readline().split()))
count = 0

if N == len(input_num):
    for num in input_num:
        if isPrime_nubmer(num):
            count += 1

print(count)


# 1번

# import sys

# N = int(sys.stdin.readline())

# input_num = list(map(int, sys.stdin.readline().split()))

# count = 0  # prime number

# if N == len(input_num):
#     for num in input_num:
#         if num == 1: # 1은 소수가 아님
#             continue

#         isPrime = True # 소수 판별
#         for i in range(2, num):
#             if num % i == 0:
#                 isPrime = False
#                 break

#         if isPrime == True:
#             count += 1

#     print(count)
