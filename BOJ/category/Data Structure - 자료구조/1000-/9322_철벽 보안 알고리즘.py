# https://www.acmicpc.net/problem/9322

import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    n = int(input())
    pk1 = input().split()
    pk2 = input().split()
    ct = input().split()

    S2P = dict()
    for i in range(n):
        S2P[pk1[i]] = i
    P2S = [0] * n
    for i in range(n):
        P2S[i] = S2P[pk2[i]]

    ans = [None] * n
    for i in range(n):
        ans[P2S[i]] = ct[i]

    print(" ".join(ans))
