def solution(s):
    return int(s)


def solution2(s):
    rst = 0

    # 받은 수 n을 역순으로
    for idx, base in enumerate(s[::-1]):
        if base == "+":
            pass
        elif base == "-":
            rst *= -1
        else:
            rst += int(base) * (10 ** idx)

    # print(rst)

    return rst


solution("+1234")
