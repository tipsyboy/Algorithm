def merge_sort(arr: list) -> None:
    def merge(start: int, end: int) -> None:
        mid = (start + end) // 2
        left, right = start, mid

        for i in range(start, end):
            if right == end:
                temp[i] = arr[left]
                left += 1
            elif left == mid:
                temp[i] = arr[right]
                right += 1
            elif arr[left] <= arr[right]:
                temp[i] = arr[left]
                left += 1
            else:
                temp[i] = arr[right]
                right += 1

        for i in range(start, end):
            arr[i] = temp[i]

    def msort(start: int, end: int) -> None:
        if start + 1 == end:
            return

        mid = (start + end) // 2

        msort(start, mid)
        msort(mid, end)
        merge(start, end)

    temp = [0] * len(arr)
    msort(0, len(arr))


test_arr = [6, -8, 1, 12, 8, 15, 7, -7]
print("og:", test_arr)
merge_sort(test_arr)
print("sorting:", test_arr)