# 2024.10.16 WED
# https://www.acmicpc.net/problem/3101

import sys

input = sys.stdin.readline
directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def sumTo(t, a, l):
    return t * (a + l) // 2


def get_start_num(top_n, bottom_n):
    u = sumTo(top_n, 1, top_n)
    v = sumTo(max(0, bottom_n - 1), N - 1, (N - 1) + (bottom_n - 2) * -1)

    return u + v + 1


def get_pos_num(x, y):
    group = x + y
    bottom = (2 * N - 1) // 2

    top_n = min(N, group)
    bottom_n = max(0, group - bottom)

    start = get_start_num(top_n, bottom_n)

    ans = 0
    if group & 1:
        ans = start + x
    else:
        ans = start + y

    if group >= N:
        ans -= bottom_n

    return ans


N, K = map(int, input().split())
command = input().rstrip()

x, y = 0, 0
ans = 1
for com in command:
    x, y = x + directions[com][0], y + directions[com][1]
    ans += get_pos_num(x, y)
print(ans)
