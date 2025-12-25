# 2024.10.19 SAT
# https://www.acmicpc.net/problem/29198

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
words = []
for _ in range(N):
    words.append("".join(sorted(input().rstrip())))
words.sort()

ans = []
for i in range(K):
    ans.extend(list(words[i]))
ans.sort()

print("".join(ans))
