# https://www.acmicpc.net/problem/15961

import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
lane = []
for _ in range(N):
    lane.append(int(input()))

sushi = [0] * (d + 1)
sushi[c] = 1
ans = 1
for i in range(k):
    if not sushi[lane[i]]:
        ans += 1
    sushi[lane[i]] += 1

cur = ans
for left in range(N):
    right = (left + k) % N

    sushi[lane[left]] -= 1
    if not sushi[lane[left]]:
        cur -= 1

    if not sushi[lane[right]]:
        cur += 1
    sushi[lane[right]] += 1

    ans = max(ans, cur)
print(ans)
