# ### 1번 풀이 (제출 코드)
def conv_to_base2(num):
    result = []

    while num > 0:
        num, r = divmod(num, 2)
        result.append(r)

    return "".join(map(str, result[::-1]))


def secret_map(n, arr1, arr2):
    conv_arr1 = []
    conv_arr2 = []
    rst = []

    #  conver to binary-number system
    for elem in arr1:
        temp = conv_to_base2(elem)
        conv_arr1.append("0" * (n - len(temp)) + temp)

    for elem in arr2:
        temp = conv_to_base2(elem)
        conv_arr2.append("0" * (n - len(temp)) + temp)

    #  bit
    for i in range(n):
        temp = ""
        for j in range(n):
            if int(conv_arr1[i][j]) or int(conv_arr2[i][j]):
                temp += "#"
            else:
                temp += " "
        rst.append(temp)

    return rst


### 2. 공부한 코드 - 더 빠름 (유의미한 속도 차이 있었음)
def secret_map2(n, arr1, arr2):
    result = []

    for num1, num2 in zip(arr1, arr2):
        temp = bin(num1 | num2)[2:]  # num1과 num2를 비트연산해서 2진수로 바꿔줌. - 10진수끼리도 비트연산 가능
        temp = temp.rjust(n, "0")
        temp = temp.replace("1", "#")
        temp = temp.replace("0", " ")
        result.append(temp)

    return result


print(secret_map2(5, [9, 1, 28, 18, 11], [30, 1, 21, 17, 28]))
