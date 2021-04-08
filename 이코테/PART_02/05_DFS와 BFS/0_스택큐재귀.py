# 재귀
def iterative_factorial(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result


def recursive_factorial(num):
    if num <= 1:
        return 1

    return num * recursive_factorial(num - 1)


print(iterative_factorial(5))
print(recursive_factorial(5))
