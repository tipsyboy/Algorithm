# 문제의 조건 추가 - 고정점은 최대 1개만 존재한다.

def get_fixed_point(arr, start, end):
    if start > end:
        return -1  # 고정점이 없는 경우

    mid = (start + end) // 2

    if mid == arr[mid]:
        return mid
    elif mid < arr[mid]:
        return get_fixed_point(arr, 0, mid - 1)
    else:
        return get_fixed_point(arr, mid + 1, end)


n = int(input())
numbers = list(map(int, input().split()))

print(get_fixed_point(numbers, 0, len(numbers) - 1))
