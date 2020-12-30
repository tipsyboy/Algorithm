# 1. 제출 코드
def solution(n):
    base3_reverse = []  #
    ans = 0

    while n > 0:
        r = n % 3  # remainder
        n = n // 3  # q

        base3_reverse.append(r)

    base3_digit = len(base3_reverse) - 1

    for idx, b in enumerate(base3_reverse):
        ans += b * (3 ** (base3_digit - idx))

    return ans


# 2.

# 10진수 num을 base진수로 변환
def convert_to_base_N(num, base):
    result = []

    while num > 0:
        num, r = divmod(num, base)
        result.append(r)

    return "".join(map(str, reversed(result)))


def solution2(n):
    base3 = convert_to_base_N(n, 3)
    base3 = base3[::-1]  # list 역순

    return int(base3, 3)  # n진수 문자열 base3를 10진수로 변환


print(solution2(45))
# solution2(125)
