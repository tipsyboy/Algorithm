# https://www.acmicpc.net/problem/15991

import sys

input = sys.stdin.readline
DIV = 1_000_000_009


def extend_dp(s: int, e: int) -> None:
    for i in range(s, e + 1):
        dp.append((dp[i - 2] + dp[i - 4] + dp[i - 6]) % DIV)


dp = [0, 1, 2, 2, 3, 3, 6]
TC = int(input())
for _ in range(TC):
    n = int(input())

    if len(dp) <= n:
        extend_dp(len(dp), n)

    print(dp[n])

"""
15991. 1, 2, 3, 더하기 6
    - 대칭이 되는 경우만 인정을 하는 '1, 2, 3, 더하기' 문제

    - 양 옆에 1, 2, 3을 더하는 경우를 생각하고 dp를 사용함
      때문에 i-2, i-4, i-6의 경우 각각에서 1, 2, 3을 양 옆에 더하는 경우의 수를 생각해주고 해결
"""