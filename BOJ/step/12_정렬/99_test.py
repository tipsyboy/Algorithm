import copy


# 1. 선택 정렬 (Selection Sort)
# 현재 값 i 를 선택한 후 i+1부터 비교를 시작해서, 가장 작은 값을 선택해서 가져온다.
def selection_sort(unsorted_list):
    copy_list = copy.deepcopy(unsorted_list)  # deep copy
    n = len(copy_list)  # 리스트 길이

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if copy_list[min_idx] > copy_list[j]:
                min_idx = j

        # swap
        copy_list[i], copy_list[min_idx] = copy_list[min_idx], copy_list[i]

    return copy_list


# 2. 삽입 정렬
# index 1부터 시작하는 key값 i로 부터 한칸씩 내려오면서 비교해서 key값이 들어갈 자리를 찾아간다.
# - 손에 들어온 카드를 오름차순으로 끼워 넣기 생각
def insertion_sort(unsorted_list):
    copy_list = copy.deepcopy(unsorted_list)
    n = len(copy_list)

    for i in range(1, n):
        # key_val = i
        for j in range(i - 1, -1, -1):
            if copy_list[j] > copy_list[j + 1]:
                copy_list[j], copy_list[j + 1] = copy_list[j + 1], copy_list[j]

    return copy_list


# 3. 버블 정렬
def bubble_sort(unsorted_list):
    copy_list = copy.deepcopy(unsorted_list)
    n = len(copy_list)

    for i in range(n - 1):
        for j in range(i, n - 1):
            if copy_list[j] > copy_list[j + 1]:
                copy_list[j], copy_list[j + 1] = copy_list[j + 1], copy_list[j]

    return copy_list


# main
unsorted_list = [9, 1, 6, 8, 4, 3, 2, 0]


print(unsorted_list)
# sorted_list = selection_sort(unsorted_list)  # 선택 정렬
# sorted_list = insertion_sort(unsorted_list)  # 삽입 정렬
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)
print(unsorted_list)
