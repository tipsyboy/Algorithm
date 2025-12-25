# https://www.acmicpc.net/problem/11899

"""
11899. 괄호 끼워넣기
    - 그냥 유명한 문제임
"""

import sys

input = sys.stdin.readline

parenthesis = input().rstrip()

stk = 0
ans = 0
for p in parenthesis:
    if p == "(":
        stk += 1
    elif p == ")":
        if stk:
            stk -= 1
        else:
            ans += 1

ans += stk
print(ans)
