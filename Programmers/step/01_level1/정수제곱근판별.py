def solution(num):
    sqrt = num ** 0.5

    ## ***
    if sqrt % 1 == 0:
        return int(sqrt + 1) ** 2

    return -1


print(solution(1234))
