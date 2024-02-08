# https://www.acmicpc.net/problem/14469

import sys

input = sys.stdin.readline

N = int(input())
cows = []
for _ in range(N):
    cows.append(tuple(map(int, input().split())))

cows.sort(key=lambda x: (x[0], x[1]), reverse=True)
time = 0
for _ in range(N):
    a, s = cows.pop()
    if time < a:
        time = a
    time += s

print(time)
