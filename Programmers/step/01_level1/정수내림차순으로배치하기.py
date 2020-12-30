def solution(num):
    rst = sorted(list(map(int, str(num))), reverse=True)

    rst = "".join(list(map(str, rst)))

    return int(rst)


def solution2(num):
    rst = sorted(str(num), reverse=True)

    return int("".join(rst))


print(solution2(118372))
