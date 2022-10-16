# https://www.acmicpc.net/problem/2870

import sys

input = sys.stdin.readline

N = int(input())

ans = []
for _ in range(N):
    word = input().rstrip()

    number = ""
    for char in word:
        if not char.isnumeric():
            if number != "":
                ans.append(int(number))
                number = ""
        else:
            number += char

    if number != "":
        ans.append(int(number))

ans.sort()
print("\n".join(map(str, ans)))
