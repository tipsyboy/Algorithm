# https://www.acmicpc.net/problem/18870

import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

new_arr = sorted(set(arr))

ans = []
mem = dict()
for i in range(N):
    if arr[i] in mem:
        ans.append(mem[arr[i]])
        continue

    rst = bisect_left(new_arr, arr[i])
    mem[arr[i]] = rst
    ans.append(rst)
print(" ".join(map(str, ans)))
