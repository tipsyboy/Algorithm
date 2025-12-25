# 2024.09.28 SAT
# https://www.acmicpc.net/problem/20413

import sys

input = sys.stdin.readline

N = int(input())
s, g, p, d = map(int, input().split())
sangmin_grades = input().rstrip()

grade = {"B": s - 1, "S": g - 1, "G": p - 1, "P": d - 1, "D": d}
money = [0] * N
money[0] = s - 1
for i in range(1, N):
    if sangmin_grades[i] == "D":
        money[i] = d
    else:
        money[i] = grade[sangmin_grades[i]] - money[i - 1]

print(sum(money))
