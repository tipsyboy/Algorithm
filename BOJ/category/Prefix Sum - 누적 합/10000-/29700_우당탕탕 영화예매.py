# 2024.11.03 SUN
# https://www.acmicpc.net/problem/29700

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

ans = 0
for _ in range(N):
    S = input().rstrip()
    cnt = 0
    for c in S:
        if c == "0":
            cnt += 1
        else:
            if cnt >= K:
                ans += cnt - K + 1
            cnt = 0
    if cnt >= K:
        ans += cnt - K + 1

print(ans)
