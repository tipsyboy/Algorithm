# Dec 15, Mon 2025
# https://www.acmicpc.net/problem/11504

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    X = int("".join(list(input().split())))
    Y = int("".join(list(input().split())))
    numbers = list(input().split())
    numbers.extend(numbers[:M])

    ans = 0
    for i in range(N):
        Z = int("".join(numbers[i : i + M]))
        if X <= Z <= Y:
            ans += 1

    print(ans)
