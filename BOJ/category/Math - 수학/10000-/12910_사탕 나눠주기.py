# 2024.08.23 FRI
# https://www.acmicpc.net/problem/12910

import sys

input = sys.stdin.readline

N = int(input())
candies = list(map(int, input().split()))
brand = [0] * 51
for candy in candies:
    brand[candy] += 1

ans = 0
for i in range(1, 51):
    if brand[i] == 0:
        break

    c = 1
    for k in range(1, i + 1):
        c *= brand[k]

    ans += c

print(ans)
