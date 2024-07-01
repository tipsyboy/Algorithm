# https://www.acmicpc.net/problem/25707

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

print((max(nums) - min(nums)) * 2)
