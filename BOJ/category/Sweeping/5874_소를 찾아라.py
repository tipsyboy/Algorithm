# 2024.07.06 SAT
# https://www.acmicpc.net/problem/5874

import sys

input = sys.stdin.readline

grass = input().rstrip()
cnt = 0
ans = 0
for i in range(len(grass) - 1):
    if grass[i] == grass[i + 1] == "(":  # 뒷다리
        cnt += 1
    elif grass[i] == grass[i + 1] == ")":  # 앞다리
        ans += cnt
print(ans)
