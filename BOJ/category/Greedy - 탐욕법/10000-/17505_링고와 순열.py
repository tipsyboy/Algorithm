# 2024.10.18 FRI
# https://www.acmicpc.net/problem/17505

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

target = N
ans = [0] * N
while K:
    if target < 1:
        ans = [-1]
        break

    back = min(K, target - 1)

    ans[N - back - 1] = target

    K -= back
    target -= 1

if ans[0] != -1:
    for i in range(N - 1, -1, -1):
        if ans[i] == 0:
            ans[i] = target
            target -= 1

print(*ans)
