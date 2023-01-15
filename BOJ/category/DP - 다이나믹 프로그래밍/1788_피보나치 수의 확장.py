# https://www.acmicpc.net/problem/1788

import sys

input = sys.stdin.readline
DIV = 1_000_000_000

N = int(input())
fibo = [0, 1]
for i in range(abs(N) - 1):
    fibo.append((fibo[-1] + fibo[-2]) % DIV)

o = 0 if N == 0 else 1
if N < 0:
    o = -1 if abs(N) % 2 == 0 else 1
print(o)
print(fibo[abs(N)])
