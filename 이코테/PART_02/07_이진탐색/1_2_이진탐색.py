# 재귀를 이용한 binary search 구현
def recur_binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recur_binary_search(arr, target, start, mid - 1)
    else:
        return recur_binary_search(arr, target, mid + 1, end)


# 반복을 이용한 binary search 구현
def iter_binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None  # 위에서 못찾은 경우 여기에 옴


#### Test
n, target = map(int, input().split())
arr = list(map(int, input().split()))

# result = recur_binary_search(arr, target, 0, n - 1)
result = iter_binary_search(arr, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
