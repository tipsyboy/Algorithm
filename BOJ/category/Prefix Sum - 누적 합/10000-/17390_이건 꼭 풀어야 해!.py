# https://www.acmicpc.net/problem/17390

"""
17390. 이건 꼭 풀어야 해!
    - 누적합 기본
"""
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)

psum = [0]
for i in range(N):
    psum.append(psum[-1] + B[i])

for _ in range(Q):
    lo, hi = map(int, input().split())
    print(psum[hi] - psum[lo - 1])
