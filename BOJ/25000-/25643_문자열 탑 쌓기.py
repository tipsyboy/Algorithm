# 2024.09.02 MON
# https://www.acmicpc.net/problem/25643

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

prev = input().rstrip()
ans = 1
for _ in range(N - 1):
    cur = input().rstrip()

    able = False
    for i in range(-M + 1, M):

        flag = True
        for j in range(M):
            if i + j < 0 or i + j >= M:
                continue

            if cur[i + j] != prev[j]:
                flag = False
                break

        if flag:
            able = True
            break

    if not able:
        ans = 0
        break

    prev = cur

print(ans)
