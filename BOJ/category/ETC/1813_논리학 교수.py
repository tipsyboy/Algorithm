# https://www.acmicpc.net/problem/1813

import sys

input = sys.stdin.readline

N = int(input())
true_cnt = [0] * 51
arr = list(map(int, input().split()))
for e in arr:
    true_cnt[e] += 1

ans = -1
for i in range(N, -1, -1):
    if true_cnt[i] == i:
        ans = i
        break
print(ans)