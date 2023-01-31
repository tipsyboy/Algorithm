# https://www.acmicpc.net/problem/2295

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

# 1)
sum_arr2 = []
for i in range(N):
    for j in range(i, N):
        sum_arr2.append(arr[i] + arr[j])
sum_arr2.sort()

# 2)
ans = -1
for i in range(N - 1, 0, -1):
    for j in range(i):
        x = arr[i] - arr[j]
        if bisect_right(sum_arr2, x) - bisect_left(sum_arr2, x):
            ans = max(ans, x + arr[j])
            break

print(ans)


"""
2295. 세 수의 합
    - 이 문제는 python으로 풀이할 때, set()을 사용해서 2) 의 과정을 log시간이 아닌 O(1)로 낮춰서 더 빠르게 돌릴 수 있음

    - 하지만 그게 중요한게 아니라 이분탐색을 사용할 때, 1)의 과정의 어떤 두 수를 묶거나 해서 
      N^x 시간을 줄여 나가는 생각 흐름이 중요하다.
"""