# 2024.09.19 THU
# https://www.acmicpc.net/problem/30458

import sys

input = sys.stdin.readline

N = int(input())
S = input().rstrip()

mid = N // 2
alphabet = [0] * 26
for i in range(mid):
    alphabet[ord(S[i]) - 97] += 1
if N & 1:
    mid += 1
for i in range(mid, N):
    alphabet[ord(S[i]) - 97] += 1

ans = "Yes"
for i in range(26):
    if alphabet[i] & 1:
        ans = "No"
print(ans)
