# 2025.01.20 MON
# https://www.acmicpc.net/problem/19939

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

mn = K * (K + 1) // 2
if N < mn:
    print(-1)
else:
    mod = (N - mn) % K
    if mod:
        print(K)
    else:
        print(K - 1)
