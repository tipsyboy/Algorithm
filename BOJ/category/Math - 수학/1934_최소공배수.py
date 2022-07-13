import sys

input = sys.stdin.readline


def gcd(a, b) -> int:
    while a > 0:
        r = b % a
        b = a
        a = r

    return b


N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))
