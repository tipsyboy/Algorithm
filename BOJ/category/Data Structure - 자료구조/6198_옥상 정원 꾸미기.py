# https://www.acmicpc.net/problem/6198

import sys

input = sys.stdin.readline

N = int(input())
building = []
for _ in range(N):
    building.append(int(input()))

ans = [0] * N
stk = []
for i in range(N - 1, -1, -1):
    while stk and building[stk[-1]] < building[i]:
        ans[i] += ans[stk.pop()] + 1

    stk.append(i)

print(sum(ans))


"""
6198. 옥상 정원 꾸미기
    - stack
"""