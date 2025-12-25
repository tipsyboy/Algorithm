# 2025.01.15 WED
# https://www.acmicpc.net/problem/2666


import sys

input = sys.stdin.readline


def door_open(idx, o1, o2):
    if idx == M:
        return 0

    if dp[o1][o2][idx] != -1:
        return dp[o1][o2][idx]

    nxt = nxts[idx]
    to_o1 = door_open(idx + 1, nxt, o2) + abs(nxt - o1)
    to_o2 = door_open(idx + 1, o1, nxt) + abs(nxt - o2)
    dp[o1][o2][idx] = min(to_o1, to_o2)

    return dp[o1][o2][idx]


N = int(input())
o1, o2 = map(int, input().split())
M = int(input())
nxts = [int(input()) for _ in range(M)]

dp = [[[-1] * (M + 1) for _ in range(N + 1)] for __ in range(N + 1)]
print(door_open(0, o1, o2))

"""
2666. 벽장문의 이동
    - 조건/상태를 고려해서 dp 테이블 설계하기 
    

    아래 두 조건의 dp 테이블이 다름을 인지해야함.
    1. dp[현재 열린문 1][현재 열린문 2][다음에 열 문 idx]
    2. dp[현재 열린문 1][현재 열린문 2][다음에 열 문 번호]
    2번의 경우 중복 번호가 발생했을 때, 실제로 최적값이 아닐수 있음.
"""
