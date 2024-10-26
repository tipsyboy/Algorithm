# 2024.10.20 SUN
# https://www.acmicpc.net/problem/29753

import sys

input = sys.stdin.readline
GRADE = {"A+": 450, "A0": 400, "B+": 350, "B0": 300, "C+": 250, "C0": 200, "D+": 150, "D0": 100, "F": 0}

N, X = input().split()
i, f = map(int, X.split("."))
X = i * 100 + f

score = 0
credit = 0
for _ in range(int(N) - 1):
    c, g = input().split()
    credit += int(c)
    score += GRADE[g] * int(c)
L = int(input())
credit += L

ans = "impossible"
for g, v in GRADE.items():
    temp = (score + v * L) // credit
    if temp > X:
        ans = g
print(ans)
