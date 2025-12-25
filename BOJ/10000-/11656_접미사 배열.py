# https://www.acmicpc.net/problem/11656

import sys

input = sys.stdin.readline

S = input().rstrip()
arr = []
for i in range(len(S)):
    arr.append(S[i:])
arr.sort()
print(*arr, sep="\n")