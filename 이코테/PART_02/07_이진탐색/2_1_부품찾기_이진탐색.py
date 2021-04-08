def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


n = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 이진탐색을 이용하기 위해 미리 정렬

m = int(input())
x = list(map(int, input().split()))

# components, part
for part in x:
    result = binary_search(arr, part, 0, n - 1)

    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
