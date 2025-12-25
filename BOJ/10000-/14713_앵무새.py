# 2025.02.27 THU
# https://www.acmicpc.net/problem/14713

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
words = []
total_words = set()
for i in range(N):
    S = input().split()
    words.append(deque(S))
    total_words.update(S)

L = input().split()
ans = "Possible"
for word in L:
    if word not in total_words:
        ans = "Impossible"
        break

    flag = False
    for w in words:
        if w and w[0] == word:
            w.popleft()
            flag = True
            break
    if not flag:
        ans = "Impossible"
        break

    total_words.remove(word)

if total_words:
    ans = "Impossible"
print(ans)
