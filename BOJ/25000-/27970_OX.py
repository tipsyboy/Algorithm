# 2024.09.24 TUE
# https://www.acmicpc.net/problem/27970

import sys

input = sys.stdin.readline
DIV = 10**9 + 7

S = input().rstrip()
bit_S = S[::-1].replace("X", "0").replace("O", "1")
print(int(bit_S, 2) % DIV)
