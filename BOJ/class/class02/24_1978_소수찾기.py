import sys
input = sys.stdin.readline

# # 1) 브루트 포스
# n = int(input())
# numbers = list(map(int, input().split()))
# count = 0  # 소수의 개수

# for num in numbers:
#     if num == 1:
#         continue
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#             break

#     if flag == True:
#         count += 1

# print(count)

# 2)
n = int(input())
numbers = list(map(int, input().split()))
count = 0

for num in numbers:
    flag = True
    if num == 1:
        continue

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            flag = False
            break

    if flag == True:
        count += 1

print(count)
