# 2024.08.05 MON
# https://www.acmicpc.net/problem/30804

import sys

input = sys.stdin.readline


def sol():
    if N == 1:
        return 1

    left, right = 0, 0
    fruit = {S[0]: 1}
    rst = 1
    while right < N - 1:
        if len(fruit) <= 2:
            right += 1
            fruit[S[right]] = fruit.get(S[right], 0) + 1
        else:
            fruit[S[left]] -= 1
            if fruit[S[left]] == 0:
                del fruit[S[left]]
            left += 1

        if len(fruit) <= 2:
            rst = max(rst, right - left + 1)

    if len(fruit) <= 2:
        rst = max(rst, right - left + 1)

    return rst


N = int(input())
S = list(map(int, input().split()))
print(sol())
