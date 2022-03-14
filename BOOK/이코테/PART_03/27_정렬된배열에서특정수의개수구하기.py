# # 1) 숫자 배열의 target을 계속 줄여나가는 방식

# # 이진탐색
# def binary_search(arr, target, start, end):
#     if start > end:
#         return None

#     mid = (start + end) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return binary_search(arr, target, start, mid-1)
#     else:
#         return binary_search(arr, target, mid+1, end)

# n, x = map(int, input().split()) # 수열의 길이, target
# numbers = list(map(int, input().split())) # 정렬된 수열
# count = 0 # target을 찾은 갯수

# # target x를 모두 찾을 때까지 찾는다.
# while True:
#     rst = binary_search(numbers, x, 0, len(numbers)-1) # 찾는다.
#     # 더 이상 찾지 못하면 break
#     if rst == None:
#         break

#     count += 1 # 카운트 증가
#     del numbers[rst] # 찾은것 삭제

# if count == 0:
#     print(-1)
# else:
#     print(count)


# # 2) 정렬된 배열이므로 target x의 시작지점, 끝점을 찾아서 갯수를 세준다.
# def count_by_value(arr, target):

#     def get_first(arr, target, start, end):
#         if start > end:
#             return None

#         mid = (start + end) // 2

#         if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
#             return mid
#         elif target <= arr[mid]:  # **** 여기 구간 조심 - 오름차순 정렬일때 맨 왼쪽을 찾기때문에 작거나 같기
#             return get_first(arr, target, start, mid-1)
#         else:
#             return get_first(arr, target, mid+1, end)

#     def get_last(arr, target, start, end):
#         if start > end:
#             return None

#         mid = (start + end) // 2

#         if (mid == len(arr)-1 or target < arr[mid + 1]) and arr[mid] == target:
#             return mid
#         elif target < arr[mid]:  # **** 여기 구간 조심 - 오름차순 정렬일때 맨 오른쪽을 찾기때문에 작은 구간
#             return get_last(arr, target, start, mid - 1)
#         else:  # **** 여기 구간 조심 - 오름차순 정렬일때 맨 오른쪽을 찾기때문에 크거나 같은 구간
#             return get_last(arr, target, mid + 1, end)

#     first = get_first(arr, target, 0, len(arr) - 1)

#     # target x을 못찾았으므로 0개 리턴
#     if first == None:
#         return 0

#     last = get_last(arr, target, 0, len(arr) - 1)

#     return last - first + 1


# n, x = map(int, input().split())
# numbers = list(map(int, input().split()))

# count = count_by_value(numbers, x)
# if count == 0:
#     print(-1)
# else:
#     print(count)


# 3) python 이진 탐색 라이브러리 bisect 사용하기
from bisect import bisect_left, bisect_right


def count_by_value(arr, target):
    left_index = bisect_left(arr, target)
    right_index = bisect_right(arr, target)

    return right_index - left_index


n, x = map(int, input().split())
numbers = list(map(int, input().split()))

count = count_by_value(numbers, x)

if not count:
    print(-1)
else:
    print(count)
