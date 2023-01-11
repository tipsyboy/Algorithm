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


numbers = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬
print("###### 선택 정렬 ######")
print(f"정렬 전: {numbers}")
print(f"정렬 후: {selection_sort(numbers)}")

# 삽입 정렬
print("###### 삽입 정렬 ######")
print(f"정렬 전: {numbers}")
print(f"정렬 후: {insertion_sort(numbers)}")
