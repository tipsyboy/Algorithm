
# f(n)을 구할 때, f(n-1)은 한 자리 즉, 1과 함께고
# f(n-2)는 두 자리 00과 함께 한다.
# 즉 f(n) = f(n-1) + f(n-2)

import sys


def zero_one_tile():
    n = int(sys.stdin.readline())

    if n == 1:
        return 1

    if n == 2:
        return 2

    numbers = [0 for i in range(n+1)]
    numbers[1] = 1
    numbers[2] = 2

    for i in range(3, n+1):
        numbers[i] = (numbers[i-1] + numbers[i-2]) % 15746

    return numbers[i]


print(zero_one_tile())
