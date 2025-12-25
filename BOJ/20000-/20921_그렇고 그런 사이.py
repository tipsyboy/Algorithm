# 2024.05.28 TUE
# https://www.acmicpc.net/problem/20921

import sys

input = sys.stdin.readline

# i < i + a and Ai > Ai+a -> 그렇고 그런 사이 (a>0)

N, K = map(int, input().split())
target = N

ans = [0] * N
while K:
    back = min(target - 1, K)

    ans[N - back - 1] = target

    target -= 1
    K -= back

for i in range(N - 1, -1, -1):
    if ans[i]:
        continue

    ans[i] = target
    target -= 1

print(*ans)
