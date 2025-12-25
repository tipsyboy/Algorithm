# https://www.acmicpc.net/problem/22862

import sys

input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
ans, now = 0, 0
while right < N:
    if arr[right] % 2 == 0:
        now += 1
        right += 1
        ans = max(ans, now)
    else:
        if K:
            K -= 1
            right += 1
        else:
            if arr[left] % 2 == 0:
                now -= 1
            else:
                K += 1
            left += 1

print(ans)
