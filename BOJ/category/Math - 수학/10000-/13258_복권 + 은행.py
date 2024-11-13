# 2024.11.05 TUE
# https://www.acmicpc.net/problem/13258

import sys

input = sys.stdin.readline

N = int(input())
balance = list(map(int, input().split()))
J = int(input())
C = int(input())

print(balance[0] + balance[0] / sum(balance) * C * J)
