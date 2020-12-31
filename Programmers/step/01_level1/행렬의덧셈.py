def matrix_add(arr1, arr2):
    rst = []

    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j] + arr2[i][j])

        rst.append(temp)

    return rst


print(matrix_add([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(matrix_add([[1], [2]], [[3], [4]]))
