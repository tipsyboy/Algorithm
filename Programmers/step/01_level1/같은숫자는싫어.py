def rm_continuos_num(arr):
    judge = arr[0]
    result = [judge]

    for i in range(1, len(arr)):
        if judge != arr[i]:
            judge = arr[i]
            result.append(judge)

    # print(result) # 확인

    return result


def rm_continuos_num2(arr):
    result = []

    for num in arr:
        if result[-1:] != [num]:
            result.append(num)

    # print(result) # 확인

    return result


rm_continuos_num2([1, 1, 3, 3, 0, 1, 1])
rm_continuos_num2([4, 4, 4, 3, 3])
rm_continuos_num2([1, 1, 1, 1, 1, 1, 1, 1, 1])
