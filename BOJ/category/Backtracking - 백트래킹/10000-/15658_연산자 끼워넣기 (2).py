# https://www.acmicpc.net/problem/15658

import sys

input = sys.stdin.readline
MAXV = float("inf")


def solution(cur: int, depth: int) -> None:
    global ans_max, ans_min

    if depth == N - 1:
        ans_max = max(ans_max, cur)
        ans_min = min(ans_min, cur)
        return

    for i in range(4):
        if not operators[i]:
            continue

        operators[i] -= 1
        if i == 0:
            solution(cur + A[depth + 1], depth + 1)
        elif i == 1:
            solution(cur - A[depth + 1], depth + 1)
        elif i == 2:
            solution(cur * A[depth + 1], depth + 1)
        elif i == 3:
            solution(int(cur / A[depth + 1]), depth + 1)
        operators[i] += 1


N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))

ans_max = -MAXV
ans_min = MAXV
solution(A[0], 0)
print(ans_max)
print(ans_min)
