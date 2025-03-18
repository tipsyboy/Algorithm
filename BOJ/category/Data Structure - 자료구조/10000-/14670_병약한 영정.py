# 2025.03.12 WED
# https://www.acmicpc.net/problem/14670

import sys

input = sys.stdin.readline

N = int(input())
medicines = dict()
for _ in range(N):
    eff, name = input().split()
    medicines[eff] = name

R = int(input())
ans = []
for _ in range(R):
    L, *S = input().split()
    rst = []
    for i in range(int(L)):
        if S[i] not in medicines:
            rst = []
            break
        rst.append(medicines[S[i]])

    if not rst:
        ans.append("YOU DIED")
    else:
        ans.append(" ".join(rst))

print(*ans, sep="\n")
