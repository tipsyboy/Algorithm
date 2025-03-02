# 2025.02.22 SAT
# https://www.acmicpc.net/problem/26070

import sys

input = sys.stdin.readline


gomgom = list(map(int, input().split()))
coupon = list(map(int, input().split()))
ans = 0
for i in range(5):
    cur = i % 3
    food = min(gomgom[cur], coupon[cur])
    gomgom[cur] -= food
    coupon[cur] -= food
    ans += food

    nxt = (cur + 1) % 3
    coupon[nxt] += coupon[cur] // 3
    coupon[cur] = coupon[cur] % 3
print(ans)


"""
26070. 곰곰이와 학식
- 모든 쿠폰이 다른 쿠폰에게 영향을 미치는 최소 회전을 생각
"""
