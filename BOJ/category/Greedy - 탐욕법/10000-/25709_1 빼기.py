# 2024.07.06 SAT
# https://www.acmicpc.net/problem/25709

import sys

input = sys.stdin.readline

N = int(input())
ans = 0
while N:

    if "1" in str(N):
        ans += str(N).count("1")
        temp = str(N).replace("1", "")
        N = 0 if temp == "" else int(temp)
    else:
        N -= 1
        ans += 1
print(ans)
