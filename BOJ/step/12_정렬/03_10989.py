# # counting sort


# 1)
# import sys


# def counting_sort(unsorted):
#     n = len(unsorted)

#     # count list
#     cnt_lst = [0 for i in range(max(unsorted) + 1)]  #

#     for item in unsorted:
#         cnt_lst[item] += 1

#     for i in range(1, len(cnt_lst)):
#         cnt_lst[i] = cnt_lst[i] + cnt_lst[i - 1]

#     # 정렬할 리스트 생성
#     sorted_lst = [0 for i in range(n)]

#     for i in range(n - 1, -1, -1):
#         x = cnt_lst[unsorted[i]] - 1
#         cnt_lst[unsorted[i]] -= 1
#         sorted_lst[x] = unsorted[i]

#     return sorted_lst

# n = int(sys.stdin.readline())  # 수의 개수
# unsorted_lst = [int(sys.stdin.readline()) for i in range(n)]  # 리스트 받기
# sorted_lst = counting_sort(unsorted_lst)

# for num in sorted_lst:
#     print(num)


# 2)
import sys

n = int(sys.stdin.readline())  # 수의 개수
cnt_lst = [0] * 10001

for i in range(n):
    cnt_lst[int(sys.stdin.readline())] += 1

for i in range(10001):
    if cnt_lst[i] != 0:
        for j in range(cnt_lst[i]):
            print(i)
