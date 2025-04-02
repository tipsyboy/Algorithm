# 2025.03.31 MON
# https://www.acmicpc.net/problem/20186

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
ans = sum(numbers[:K]) - K * (K - 1) // 2
print(ans)
