# 2024.07.04 THU
# https://www.acmicpc.net/problem/2865

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
max_scores = [0] * N
for i in range(M):
    scores = input().split()
    for j in range(0, N * 2, 2):
        c = int(scores[j]) - 1
        s = float(scores[j + 1])

        if max_scores[c] < s:
            max_scores[c] = s

max_scores.sort()
print(f"{sum(max_scores[N - K :]):.1f}")
