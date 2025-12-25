# https://www.acmicpc.net/problem/1920

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


# def bi(A: list, target: int) -> int:
#     lo, hi = 0, len(A) - 1

#     while lo <= hi:
#         mid = (lo + hi) // 2

#         if target == A[mid]:
#             return 1
#         elif target < A[mid]:
#             hi = mid - 1
#         else:
#             lo = mid + 1

#     return 0


N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

for target in arr:
    if bisect_right(A, target) - bisect_left(A, target):
        print(1)
    else:
        print(0)