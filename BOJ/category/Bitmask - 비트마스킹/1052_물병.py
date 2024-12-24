# 2024.11.29 FRI
# https://www.acmicpc.net/problem/1052

import sys

input = sys.stdin.readline


def count_bit_by_num(num):
    cnt = 0
    for i in range(num.bit_length()):
        if num & (1 << i):
            cnt += 1

    return cnt


N, K = map(int, input().split())
idx = 0
ans = 0
while count_bit_by_num(N) > K:
    while idx < N.bit_length():
        if N & (1 << idx):
            N += 1 << idx
            ans += 1 << idx
            break
        idx += 1

print(ans)
