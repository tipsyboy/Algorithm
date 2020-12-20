def get_divided_num(arr, divisor):
    result = []

    for num in arr:
        if num % divisor == 0:
            result.append(num)

    if not result:
        result.append(-1)

    return sorted(result)


def get_divided_num2(arr, divisor):

    return sorted([x for x in arr if x % divisor == 0]) or [-1]


# test case
print(get_divided_num([5, 9, 7, 10], 5))
print(get_divided_num([2, 36, 1, 3], 1))
print(get_divided_num([3, 2, 6], 10))
