# 2024.10.22 TUE
# https://www.acmicpc.net/problem/1544

import sys

input = sys.stdin.readline

N = int(input())
words = set()
for _ in range(N):
    word = input().rstrip()

    temp = []
    for i in range(len(word)):
        new_word = word[i:] + word[:i]
        temp.append(new_word)

    temp.sort()

    words.add(temp[0])

print(len(words))
