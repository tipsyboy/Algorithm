# 2024.07.10 WED
# https://www.acmicpc.net/problem/30020

import sys

input = sys.stdin.readline

A, B = map(int, input().split())

ans = []
while A > 1 and B > 0 and B < A:
    if A == B + 1:
        ans.append(B)
        A, B = 0, 0
        break

    ans.append(1)
    A -= 2
    B -= 1

if A or B:
    print("NO")
else:
    print("YES")
    print(len(ans))
    for i in range(len(ans)):
        print("ab" * ans[i] + "a")
