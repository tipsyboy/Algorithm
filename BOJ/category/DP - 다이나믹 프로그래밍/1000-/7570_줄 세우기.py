# https://www.acmicpc.net/problem/7570
"""
7570. 줄 세우기
    - 다시 풀어보기

    - 단순 LIS라고 생각했으나, 아니고 
      문제에 조건에 맞추려면 연속되는 가장 긴 부분수열을 찾아야함. 
      따라서 i번째 이전의 경우에 (i-1, i-2, i-3 ...) a[i]-1 이 있었는지를 찾아야한다.

    - Longest Continuously Increasing Subsequence
"""


import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0] * (N + 1)
for i in range(N):
    dp[arr[i]] = dp[arr[i] - 1] + 1

print(N - max(dp))


