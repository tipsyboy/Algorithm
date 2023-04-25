# https://www.acmicpc.net/problem/9507

import sys

input = sys.stdin.readline


fibo = [1, 1, 2, 4]
for i in range(4, 68):
    fibo.append(fibo[i - 1] + fibo[i - 2] + fibo[i - 3] + fibo[i - 4])

t = int(input())
for _ in range(t):
    n = int(input())
    print(fibo[n])

"""
9507. Generations of Tribbles
    - 하라는대로 하면됨
"""