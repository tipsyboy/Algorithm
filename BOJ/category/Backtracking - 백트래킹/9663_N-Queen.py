# https://www.acmicpc.net/problem/9663

import sys

input = sys.stdin.readline


def n_queen(row: int) -> None:
    global ans

    if row == N:
        ans += 1
        return

    for col in range(N):
        if visited_col[col] or visited_diag_up[row + col] or visited_diag_down[row - col + N - 1]:
            continue

        visited_col[col] = True
        visited_diag_up[row + col] = True
        visited_diag_down[row - col + N - 1] = True
        n_queen(row + 1)
        visited_col[col] = False
        visited_diag_up[row + col] = False
        visited_diag_down[row - col + N - 1] = False


N = int(input())
visited_col = [False] * N
visited_diag_up = [False] * (2 * N + 1)
visited_diag_down = [False] * (2 * N + 1)
ans = 0
n_queen(0)
print(ans)
