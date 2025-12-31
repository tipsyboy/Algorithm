# Dec 10, Wed 2025
# https://www.acmicpc.net/problem/9047

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = input().rstrip()
    cur = N
    stage = 0
    while cur != "6174":
        list_N = list(cur)
        list_N.sort()
        nxt = int("".join(list_N[::-1])) - int("".join(list_N))
        cur = str(nxt).zfill(4)
        stage += 1

    print(stage)
