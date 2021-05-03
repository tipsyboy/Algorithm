# 1) python의 slicing을 이용한 회전
def rotate_1(arr, n):
    # 1.
    if not arr:
        return arr

    n %= len(arr)  # len(arr)*x바퀴 만큼 돌아오는 경우 방지
    if not n:
        return arr

    # 2.
    left = arr[:-n]
    right = arr[-n:]

    # 3.
    return right + left


# 2) 배열 값 이동을 통한 회전
def rotate_2(arr, n):
    # 1.
    if not arr:
        return arr

    # 2.
    length = len(arr)
    n %= length
    if not n:
        return arr

    new_arr = [None for _ in range(length)]

    # arr index 범위를 넘어서는 값을 위해 나머지 연산
    for i in range(length):
        new_arr[(i + n) % length] = arr[i]

    return new_arr


# 3) Reverse the reversed
def reverse(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[len(arr) - i - 1])

    return new_arr


def rotate_3(arr, n):
    # 1)
    # 예외 처리
    # arr이 없는 경우
    if not arr:
        return arr

    length = len(arr)
    n %= length
    # arr의 길이만큼 돌려서 돌릴 필요가 없는 경우
    if not n:
        return arr

    left, right = [], []

    # 2)
    # left right 구하기 by slicing
    # left = reverse(arr[:-n])
    # right = reverse(arr[-n:])

    # left right 구하기 by indexing
    for i in range(length - n):
        left.append(arr[i])
    for i in range(length - n, length):
        right.append(arr[i])

    left_rev = reverse(left)
    right_rev = reverse(right)

    # 3)
    # rev들을 합치고 다시 reverse해서 리턴한다.
    return reverse(left_rev + right_rev)


# 4) juggling - 개념이 잘 이해가 안됨... 일단 넘어감
def rotate_4(arr, n):
    pass


# 5) 분할정복 기법 - 어렵다... 다시..
def swap(arr, h, t, size):
    # 1.
    if h > t:
        swap(arr, t, h, size)

    if h + size > t:
        raise IndexError("Swap range is duplicated!")

    temp = [None for _ in range(size)]

    for i in range(size):
        temp[i] = arr[h + i]
        arr[h + i] = arr[t + i]
        arr[t + i] = temp[i]

    return


def rotate_5(arr, n):
    if not arr:
        return arr

    length = len(arr)
    n %= length
    if not n:
        return arr

    def solve(lo, mid, hi):
        # 세 경우의 수를 따지려면 먼저 left와 right의 길이를 알아야함.
        left_size = mid - lo + 1
        right_size = hi - mid

        # arr의 left와 right의 길이가 같은 경우
        if left_size == right_size:
            swap(arr, lo, mid + 1, left_size)
            return

        # left가 긴 경우
        if left_size > right_size:
            swap(arr, lo, mid + 1, right_size)
            solve(lo + right_size, mid, hi)
        # right가 긴 경우
        else:
            swap(arr, lo, hi - left_size + 1, left_size)
            solve(lo, mid, hi - left_size)

    solve(0, length - n - 1, length - 1)
    return arr


arr = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(rotate_5(arr2, 3))
