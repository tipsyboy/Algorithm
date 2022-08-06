# 24060 알고리즘 수업 - 병합 정렬 1
import sys

input = sys.stdin.readline


def merge(arr: list, start: int, mid: int, end: int) -> None:
    global cnt, ans

    temp = [0] * (end - start + 1)
    left, right, idx = start, mid + 1, 0

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            temp[idx] = arr[left]
            left += 1
        else:
            temp[idx] = arr[right]
            right += 1

        idx += 1

    while left <= mid:
        temp[idx] = arr[left]
        idx += 1
        left += 1

    while right <= end:
        temp[idx] = arr[right]
        idx += 1
        right += 1

    idx = start
    for i in range(end - start + 1):
        arr[idx] = temp[i]
        cnt += 1
        if cnt == K:
            ans = temp[i]
            return
        idx += 1


def merge_sort(arr: list, start: int, end: int) -> None:
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)
    if ans != -1:
        return


N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
ans = -1
merge_sort(arr, 0, len(arr) - 1)
print(ans)