# https://www.acmicpc.net/problem/25822

import sys

input = sys.stdin.readline

C = float(input())
N = int(input())
solved = list(map(int, input().split()))

freeze = int(C // 0.99) if C // 0.99 < 2 else 2
left, right, p = 0, 0, 0
no_solved = []
ans = 0
while right < N:
    if solved[right] == 0:
        no_solved.append(right)

        if freeze:
            freeze -= 1
        else:
            ans = max(ans, right - left)
            left = no_solved[p] + 1
            p += 1

    right += 1

ans = max(ans, right - left)
print(ans)
print(max(solved))
