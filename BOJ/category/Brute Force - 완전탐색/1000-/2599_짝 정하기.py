# 2025.03.11 TUE
# https://www.acmicpc.net/problem/2599

import sys

input = sys.stdin.readline


N = int(input())
AM, AF = map(int, input().split())
BM, BF = map(int, input().split())
CM, CF = map(int, input().split())
if AM > BF + CF or BM > AF + CF or CM > AF + BF:
    print(0)
else:
    for i in range(AM):
        ab = i
        ac = AM - i
        bc = CF - ac
        ba = BM - bc
        ca = AF - ba
        cb = BF - i

        if ba < 0 or bc < 0 or ca < 0 or cb < 0:
            continue
        print(1)
        print(ab, ac)
        print(ba, bc)
        print(ca, cb)
        break
