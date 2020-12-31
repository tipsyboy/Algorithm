def solution(num):
    if num == 1:
        return 0

    for i in range(500):
        if not num % 2:
            num = num // 2
        else:
            num = (num * 3) + 1

        if num == 1:
            return i + 1

    return -1


print(solution(626331))
