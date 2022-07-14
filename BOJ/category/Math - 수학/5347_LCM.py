import sys

input = sys.stdin.readline


def gcd(a: int, b: int) -> int:
    while a:
        r = b % a
        b = a
        a = r

    return b


TC = int(input())
for _ in range(TC):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))


"""
5347. LCM
    - 유클리드 호제법
    - lcm = a * b // gcd(a, b)
"""