# https://www.acmicpc.net/problem/12847

"""
12847. 꿀 아르바이트
    1. 연속하는 m개의 수가 최대인 값을 구해야함
    2. n의 범위가 10^5 이므로 O(N^2)에는 해결할 수 없음
    3. 누적합을 사용함. 
"""


import sys

input = sys.stdin.readline


def sol(n: int, m: int, T: list) -> int:
    if m == 0:
        return 0

    psum = [0]
    for i in range(n):
        psum.append(psum[-1] + T[i])
    ans = max(psum[: m + 1])
    for i in range(m + 1, n + 1):
        if psum[i] - psum[i - m] > ans:
            ans = psum[i] - psum[i - m]

    return ans


n, m = map(int, input().split())
T = list(map(int, input().split()))
print(sol(n, m, T))