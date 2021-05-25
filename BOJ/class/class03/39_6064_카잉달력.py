import sys
input = sys.stdin.readline


def gcd(a, b):
    while b != 0:
        n = a % b
        a = b
        b = n

    return a


t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    if m == x:
        x = 0
    if n == y:
        y = 0

    rst = -1
    lcm = m * n // gcd(m, n)  # 최소 공배수

    for i in range(x, lcm + 1, m):
        if i % n == y:
            rst = i
            break

    print(rst)
