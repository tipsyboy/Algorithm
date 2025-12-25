# https://www.acmicpc.net/problem/13413

import sys

input = sys.stdin.readline


def sol() -> None:
    T = int(input())
    for _ in range(T):
        N = int(input())
        init = input().rstrip()
        want = input().rstrip()

        w, b = 0, 0
        for i in range(N):
            if init[i] == want[i]:
                continue

            if want[i] == "W":
                w += 1
            else:
                b += 1

        print(max(w, b))


sol()
