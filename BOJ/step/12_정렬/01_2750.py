# 1)
import sys


# 선택 정렬
def selection_sort(unsorted, N):
    for i in range(N - 1):
        min_idx = i

        for j in range(i + 1, N):
            if unsorted[min_idx] > unsorted[j]:
                min_idx = j

        unsorted[min_idx], unsorted[i] = unsorted[i], unsorted[min_idx]  # swap

    return unsorted


# 삽입 정렬
def insertion_sort(unsorted, N):
    for i in range(1, N):
        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]

    return unsorted


# 버블 정렬
def bubble_sort(unsorted, N):
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

    return unsorted


N = int(sys.stdin.readline())  # 수의 개수ㅡ
unsorted_list = [int(sys.stdin.readline()) for i in range(N)]  # 리스트 입력 받음

selection_sort(unsorted_list, N)

for elem in unsorted_list:
    print(elem)

# # 2)
# import sys

# N = int(sys.stdin.readline())

# sorted_list = []

# for i in range(N):
#     sorted_list.append(int(sys.stdin.readline()))

# sorted_list.sort()

# for num in sorted_list:
#     print(num)
