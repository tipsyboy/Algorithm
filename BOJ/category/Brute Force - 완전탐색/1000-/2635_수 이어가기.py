# 2024.11.12 TUE
# https://www.acmicpc.net/problem/2635

import sys

input = sys.stdin.readline

first = int(input())
mx_len = -1
ans = []
for second in range(first):
    nums = [first, second]
    while nums[-1] >= 0:
        nums.append(nums[-2] - nums[-1])

    if mx_len < len(nums[:-1]):
        mx_len = len(nums[:-1])
        ans = nums[:-1]

print(mx_len)
print(*ans)
