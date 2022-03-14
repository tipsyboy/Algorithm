# """
# 1번 코드
# 전통적인 방식의 quick sort 구현
# """


# def quick_sort(arr, start, end):
#     # 종료 조건 - 리스트의 원소가 하나이거나 잘못된 index로 들어온 start와 end
#     if start >= end:
#         return

#     pivot = start
#     left = start + 1
#     right = end

#     # 역/이/대우
#     # 엇갈릴때까지 돌아야 하므로 left > right의 역
#     while left <= right:
#         while left <= end and arr[pivot] >= arr[left]:
#             left += 1

#         while right > start and arr[pivot] <= arr[right]:
#             right -= 1

#         if left > right:
#             arr[pivot], arr[right] = arr[right], arr[pivot]
#         else:
#             arr[left], arr[right] = arr[right], arr[left]

#     quick_sort(arr, start, right - 1)
#     quick_sort(arr, right + 1, end)


# arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# print(f"[정렬 전] {arr}")
# quick_sort(arr, 0, len(arr) - 1)
# print(f"[정렬 후] {arr}")


# 2번 코드

"""
파이썬의 장점을 살린 코드
좀 더 직관적으로 볼 수 있으나,
피벗의 비교 연산 횟수가 증가해서 시간 면에서 손해가 있다.
"""


def quick_sort2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 첫 번째 원소가 pivot이 된다.
    tail = arr[1:]  # pivot을 제외한 나머지

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

print(f"[정렬 전] {arr}")
print(f"[정렬 후] {quick_sort2(arr)}")
