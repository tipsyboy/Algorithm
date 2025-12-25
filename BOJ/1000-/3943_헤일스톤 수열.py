# https://www.acmicpc.net/problem/3943

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())

    ans = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1

        if n > ans:
            ans = n

    print(ans)
