array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print(f"[정렬 전] {array}")

for i in range(len(array) - 1):
    idx_min = i
    for j in range(i + 1, len(array)):
        if array[idx_min] > array[j]:
            idx_min = j
    array[i], array[idx_min] = array[idx_min], array[i]

print(f"[정렬 후] {array}")
