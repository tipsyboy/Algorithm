# 2024.07.29 MON
# https://www.acmicpc.net/problem/26123

import sys

input = sys.stdin.readline

N, D = map(int, input().split())
buildings = list(map(int, input().split()))
cnt = dict()
for building in buildings:
    cnt[building] = cnt.get(building, 0) + 1

ans = 0
max_height = max(cnt)
for _ in range(D):
    if max_height == 0:
        break
    ans += cnt[max_height]
    cnt[max_height - 1] = cnt.get(max_height - 1, 0) + cnt.get(max_height, 0)
    del cnt[max_height]
    max_height = max_height - 1
print(ans)
