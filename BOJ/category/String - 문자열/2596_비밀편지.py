# https://www.acmicpc.net/problem/2596

import sys

input = sys.stdin.readline

decoder = {
    "A": "000000",
    "B": "001111",
    "C": "010011",
    "D": "011100",
    "E": "100110",
    "F": "101001",
    "G": "110101",
    "H": "111010",
}

N = int(input())
word = input().rstrip()

ans = ""
for i in range(0, N * 6, 6):
    char = word[i : i + 6]
    cnt = [0] * 8

    for c in range(65, 73):
        candidate = decoder[chr(c)]
        for j in range(len(char)):
            if char[j] != candidate[j]:
                cnt[c - 65] += 1

    minv = min(cnt)
    if minv > 1:
        ans = i // 6 + 1
        break

    ans += chr(cnt.index(minv) + 65)
print(ans)
