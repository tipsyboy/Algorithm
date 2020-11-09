# #1)
import sys


def merge_sort(unsorted):
    # 리스트의 길이가 1보다 작으면 정렬할 필요가 없다.
    if len(unsorted) <= 1:
        return

    mid = len(unsorted) // 2
    left = unsorted[:mid]
    right = unsorted[mid:]
    merge_sort(left)
    merge_sort(right)

    left_idx = 0
    right_idx = 0
    idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            unsorted[idx] = left[left_idx]
            idx += 1
            left_idx += 1
        else:
            unsorted[idx] = right[right_idx]
            idx += 1
            right_idx += 1

    while left_idx < len(left):
        unsorted[idx] = left[left_idx]
        idx += 1
        left_idx += 1

    while right_idx < len(right):
        unsorted[idx] = right[right_idx]
        idx += 1
        right_idx += 1


N = int(sys.stdin.readline())
unsorted_list = [int(sys.stdin.readline()) for i in range(N)]
merge_sort(unsorted_list)
for i in range(N):
    print(unsorted_list[i])


# #2)
# import sys

# N = int(sys.stdin.readline())
# sorted_list = []

# for i in range(N):
#     sorted_list.append(int(sys.stdin.readline()))

# sorted_list.sort()  # 오름차순 정렬

# for num in sorted_list:
#     print(num)
