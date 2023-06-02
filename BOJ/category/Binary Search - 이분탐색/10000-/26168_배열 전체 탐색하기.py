# https://www.acmicpc.net/problem/26168

"""
26168. 배열 전체 탐색하기
    - 정렬 후 쿼리를 해결
    - 1<= n, m <= 100_000 이므로 선형시간엔 안됨
    - 이분탐색을 사용
"""

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
for _ in range(m):
    com, *k = map(int, input().split())
    if com == 1:
        print(n - bisect_left(arr, k[0]))
    elif com == 2:
        print(n - bisect_right(arr, k[0]))
    elif com == 3:
        print(bisect_right(arr, k[1]) - bisect_left(arr, k[0]))
