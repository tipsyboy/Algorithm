def convert_numeral_system(number, base):
    T = "0123456789ABCDEF"

    q, r = divmod(number, base)

    return convert_numeral_system(q, base) + T[r] if q else T[r]


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


def solution(n, k):
    k_base = convert_numeral_system(n, k)
    rst = 0
    for num in k_base.split("0"):
        if num == "":
            continue

        if not is_prime(int(num)):
            continue

        rst += 1

    return rst


"""
    - 딱히 볼게 없음
    - 진수 변환, 소수 판별 알고리즘
"""