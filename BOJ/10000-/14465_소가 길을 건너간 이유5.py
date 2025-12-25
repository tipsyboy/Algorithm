# https://www.acmicpc.net/problem/14465
# 2022-08-10 TUE

import sys

input = sys.stdin.readline

N, K, B = map(int, input().split())
broken = [0] * (N + 1)

for _ in range(B):
    broken[int(input())] = 1

psum = [0]
for i in range(1, N + 1):
    psum.append(psum[-1] + broken[i])

ans = float("inf")
for i in range(K, N + 1):
    ans = min(ans, psum[i] - psum[i - K])

print(ans)

"""
14465. 소가 길을 건나긴 이유 5
    - 누적합 / 슬라이딩 윈도우 / 투 포인터
"""