# https://www.acmicpc.net/problem/9517

import sys

input = sys.stdin.readline

K = int(input()) - 1
N = int(input())
time = 0
for _ in range(N):
    s, rst = input().split()
    time += int(s)
    if time >= 210:
        break

    if rst == "T":
        K = (K + 1) % 8

print(K + 1)


"""
9517. 아이 러브 크로아티아
    - 그냥 하라는대로 시뮬레이션 돌림
"""