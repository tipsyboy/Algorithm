# Dec 8, Mon 2025
# https://www.acmicpc.net/problem/1448

import sys

input = sys.stdin.readline

N = int(input())
length_list = [int(input()) for _ in range(N)]
length_list.sort(reverse=True)
ans = -1
for i in range(N - 2):
    if length_list[i] >= length_list[i + 1] + length_list[i + 2]:
        continue
    ans = length_list[i] + length_list[i + 1] + length_list[i + 2]
    break
print(ans)
