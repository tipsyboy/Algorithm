# https://www.acmicpc.net/problem/1051

import sys

input = sys.stdin.readline


def is_exist(x: int) -> bool:
    for i in range(N - x + 1):
        for j in range(M - x + 1):
            if rect[i][j] == rect[i + x - 1][j] == rect[i][j + x - 1] == rect[i + x - 1][j + x - 1]:
                return True

    return False


N, M = map(int, input().split())
rect = [list(map(int, input().rstrip())) for _ in range(N)]

ans = 1
for x in range(2, min(N, M) + 1):
    if is_exist(x):
        ans = x

print(ans ** 2)
