# 2024.10.03 THU
# https://www.acmicpc.net/problem/1897

import sys

input = sys.stdin.readline


d, init_word = input().split()
words = [input().rstrip() for _ in range(int(d))]
words.sort(key=lambda x: len(x))

visited = set([init_word])
ans = init_word
for word in words:
    for i in range(len(word)):
        cand = word[:i] + word[i + 1 :]

        if cand in visited:
            visited.add(word)
            if len(word) > len(ans):
                ans = word

print(ans)
