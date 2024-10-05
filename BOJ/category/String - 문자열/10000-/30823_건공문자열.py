# https://www.acmicpc.net/problem/30823

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
word = input().rstrip()

ans = word[K - 1 :]
if (N - K + 1) & 1:
    ans += word[: K - 1][::-1]
else:
    ans += word[: K - 1]
print(ans)
