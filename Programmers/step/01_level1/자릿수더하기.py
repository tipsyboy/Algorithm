def solution(n):
    rst = 0
    num = str(n)

    for i in range(len(num)):
        rst += int(num[i])

    return rst


def solution2(n):
    rst = list(map(int, str(n)))

    return sum(rst)


print(solution2(1234))
