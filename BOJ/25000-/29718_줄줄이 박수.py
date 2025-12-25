# 2024.07.11 THU
# https://www.acmicpc.net/problem/29718

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
A = int(input())

col_sum = []
for col in range(M):
    temp = 0
    for row in range(N):
        temp += grid[row][col]
    col_sum.append(temp)

psum = [0]
for i in range(M):
    psum.append(psum[-1] + col_sum[i])

ans = -1
for i in range(M + 1 - A):
    sec_sum = psum[i + A] - psum[i]
    if sec_sum > ans:
        ans = sec_sum
print(ans)
