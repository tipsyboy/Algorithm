# https://www.acmicpc.net/problem/16139

import sys

input = sys.stdin.readline

S = input().rstrip()

alpha = [[0] * 26]
for i in range(len(S)):
    temp = alpha[i].copy()
    temp[ord(S[i]) % 97] += 1
    alpha.append(temp)

q = int(input())
for _ in range(q):
    char, l, r = input().split()

    c = ord(char) % 97
    l, r = int(l), int(r)
    print(alpha[r + 1][c] - alpha[l][c])
