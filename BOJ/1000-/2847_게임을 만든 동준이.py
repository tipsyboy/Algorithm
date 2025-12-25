# https://www.acmicpc.net/problem/2847

import sys

input = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

ans = 0
for i in range(N - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        ans += scores[i] - (scores[i + 1] - 1)
        scores[i] = scores[i + 1] - 1

print(ans)


"""
2847. 게임을 만든 동준이
    - 뒤에서부터 훑어주면서 그리디하게 하면됨
"""