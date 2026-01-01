# Dec 25, Thu 2025
# https://www.acmicpc.net/problem/2740

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix1 = []
for _ in range(N):
    matrix1.append(list(map(int, input().split())))
M, K = map(int, input().split())
matrix2 = []
for _ in range(M):
    matrix2.append(list(map(int, input().split())))


ans = [[0] * K for _ in range(N)]
for a in range(N):
    for b in range(M):
        for c in range(K):
            ans[a][c] += matrix1[a][b] * matrix2[b][c]

for i in range(N):
    print(*ans[i])
