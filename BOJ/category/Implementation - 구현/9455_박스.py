# https://www.acmicpc.net/problem/9455

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]

    ans = 0
    for i in range(n):
        target = m - 1
        for j in range(m):
            if grid[j][i] == 1:
                ans += target - j
                target -= 1

    print(ans)
