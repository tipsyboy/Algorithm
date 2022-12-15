# https://www.acmicpc.net/problem/2491

import sys

input = sys.stdin.readline


N = int(input())
numbers = list(map(int, input().split()))

dp_up = [1] * len(numbers)
dp_down = [1] * len(numbers)
for i in range(1, len(numbers)):
    if numbers[i] >= numbers[i - 1]:
        dp_up[i] = dp_up[i - 1] + 1

for i in range(1, len(numbers)):
    if numbers[i] <= numbers[i - 1]:
        dp_down[i] = dp_down[i - 1] + 1

print(max(max(dp_up), max(dp_down)))