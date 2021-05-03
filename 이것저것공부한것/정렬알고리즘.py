import copy


# 선택정렬
def selection_sort(numbers):
    temp = copy.deepcopy(numbers)

    for i in range(len(temp) - 1):
        min_index = i  # 자기 자신이 최소 값으로 선택 될 수도 있다.
        for j in range(i, len(temp)):
            if temp[min_index] > temp[j]:
                min_index = j

        temp[i], temp[min_index] = temp[min_index], temp[i]

    return temp


# 삽입 정렬
def insertion_sort(numbers):
    temp = copy.deepcopy(numbers)

    for i in range(1, len(temp)):
        for j in range(i, 0, -1):
            if temp[j] < temp[j - 1]:
                temp[j], temp[j - 1] = temp[j - 1], temp[j]
            else:
                break

    return temp


# 퀵소트
def quick_sort(numbers, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        # left side
        while left <= end and numbers[pivot] >= numbers[left]:
            left += 1

        # right side
        while right > start and numbers[pivot] <= numbers[right]:
            right -= 1

        # 완전히 엇갈린 경우
        if left > right:
            numbers[pivot], numbers[right] = numbers[right], numbers[pivot]
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]

    quick_sort(numbers, start, right - 1)
    quick_sort(numbers, right + 1, end)


numbers = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬
print("###### 선택 정렬 ######")
print(f"정렬 전: {numbers}")
print(f"정렬 후: {selection_sort(numbers)}")

# 삽입 정렬
print("###### 삽입 정렬 ######")
print(f"정렬 전: {numbers}")
print(f"정렬 후: {insertion_sort(numbers)}")

# 퀵 소트
print("###### 퀵 소트 ######")
copy_numbers = copy.deepcopy(numbers)
print(f"정렬 전: {copy_numbers}")
quick_sort(copy_numbers, 0, len(copy_numbers) - 1)
print(f"정렬 후: {copy_numbers}")
