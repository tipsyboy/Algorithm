# 2024.09.08 SUN
# https://www.acmicpc.net/problem/20114

import sys

input = sys.stdin.readline

N, H, W = map(int, input().split())
word = [list(input().rstrip()) for _ in range(H)]

ans = ["?"] * N
for s in range(0, N * W, W):
    for i in range(s, s + W):
        for j in range(H):
            if word[j][i] == "?":
                continue
            ans[s // W] = word[j][i]
print("".join(ans))
