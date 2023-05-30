# https://www.acmicpc.net/problem/27496

"""
27496. 발머의 피크 이론
    - 그냥 하면됨
    - 실수 오차 때문에 헤맸는데, 실수표현시 정수로 표현이 가능하면 정수로 표현해서 실수오차를 없애자
"""

import sys

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

C, ans = 0, 0
for i in range(N):
    C += A[i]
    if i > L - 1:
        C -= A[i - L]

    if 129 <= C <= 138:
        ans += 1

print(ans)
