# https://www.acmicpc.net/problem/4796

import sys

input = sys.stdin.readline

case = 1
while True:
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    if V % P >= L:
        print("Case %d: %d" % (case, V // P * L + L))
    else:
        print("Case %d: %d" % (case, V // P * L + V % P))

    case += 1
