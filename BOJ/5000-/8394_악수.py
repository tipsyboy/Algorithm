# 2025.01.04 SAT
# https://www.acmicpc.net/problem/8394

"""
8394. 악수
    - 점화식 세우기
    - 메모리 아끼기
    - 마지막 자리만 출력
"""
import sys

input = sys.stdin.readline

n = int(input())
dp = [1, 2, 3]
for i in range(3, n):
    v = (dp[-1] + dp[-2]) % 10
    dp[0] = dp[1]
    dp[1] = dp[2]
    dp[2] = v

if n == 1:
    print(dp[0])
elif n == 2:
    print(dp[1])
else:
    print(dp[2])
