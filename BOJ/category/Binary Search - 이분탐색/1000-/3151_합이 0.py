# https://www.acmicpc.net/problem/3151

import sys
from bisect import bisect_left

input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

arr.sort()
print(arr)
ans = 0
for i in range(N):
    lo, hi = i + 1, N - 1
    while lo < hi:
        v = arr[i] + arr[lo] + arr[hi]

        if v > 0:
            hi -= 1
        elif v < 0:
            lo += 1
        else:
            if arr[lo] == arr[hi]:
                ans += hi - lo
            else:
                ans += hi - bisect_left(arr, arr[hi]) + 1
            lo += 1

print(ans)


"""
3151. 합이 0
    - 이전에 풀었던 이분탐색 연습문제는 중복이 가능했으나, 이번 문제는 중복이 불가능하다. 
      때문에 중복여부를 확인해야 하고, 이 경우에는 포인터를 사용하는 것처럼 사용함
"""