# 2024.08.29 THU
# https://www.acmicpc.net/problem/1972

import sys

input = sys.stdin.readline

while True:
    word = input().rstrip()

    if word == "*":
        break

    unique = True
    for i in range(len(word)):
        unique_set = set()
        unique = True

        for j in range(len(word) - i - 1):
            pair = word[j] + word[j + i + 1]

            if pair in unique_set:
                unique = False
                break

            unique_set.add(pair)

        if not unique:
            break

    if unique:
        print(f"{word} is surprising.")
    else:
        print(f"{word} is NOT surprising.")
