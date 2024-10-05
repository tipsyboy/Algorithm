# 2024.08.07 WED
# https://www.acmicpc.net/problem/5637

import sys

input = sys.stdin.readline

ans = ""
while True:
    sentence = input().split()

    end = False
    for split_by_blank in sentence:
        if split_by_blank == "E-N-D":
            end = True
            break

        word = ""
        word_list = []
        for char in split_by_blank:
            if char.isalpha() or char == "-":
                word += char
            else:
                word_list.append(word)
                word = ""
        if word != "":
            word_list.append(word)

        longest = max(word_list, key=lambda x: len(x))
        if len(longest) > len(ans):
            ans = longest

    if end:
        break

print(ans.lower())
