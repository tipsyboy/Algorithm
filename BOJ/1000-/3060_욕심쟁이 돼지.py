# Dec 9, Tue 2025
# https://www.acmicpc.net/problem/3060

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    need = list(map(int, input().split()))

    day = 1
    while sum(need) <= N:
        new_need = [0] * 6
        for i in range(6):
            new_need[i] = need[i] + need[(i - 1) % 6] + need[(i + 1) % 6] + need[(i + 3) % 6]
        need = new_need
        day += 1

    print(day)
