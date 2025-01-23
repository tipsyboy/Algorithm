# 2025.01.10 FRI
# https://www.acmicpc.net/problem/4883

import sys

input = sys.stdin.readline

k = 1
while True:
    N = int(input())
    if N == 0:
        break

    G = []
    for _ in range(N):
        G.append(list(map(int, input().split())))

    D = [[0] * 3 for _ in range(N)]
    D[0] = [G[0][1], G[0][1], G[0][2] + G[0][1]]
    for i in range(1, N):
        for j in range(3):
            if j == 0:
                D[i][j] = G[i][j] + min(D[i - 1][j], D[i - 1][j + 1])
            elif j == 1:
                D[i][j] = G[i][j] + min(D[i][j - 1], D[i - 1][j - 1], D[i - 1][j], D[i - 1][j + 1])
            else:
                D[i][j] = G[i][j] + min(D[i][j - 1], D[i - 1][j - 1], D[i - 1][j])

    print(f"{k}. {D[N-1][1]}")
    k += 1
