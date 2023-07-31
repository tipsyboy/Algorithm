# https://www.acmicpc.net/problem/11582

"""
11582. 치킨 TOP
    - 구간 정렬로 파이썬 슬라이싱을 이용하면 좀 더 쉽게 해결할 수 있지만, 머지소트를 사용해서 해결해봄
    
    - 문제의 조건에 맞게 머지소트를 어디까지 수행해야 하는가가 문제
"""


import sys

input = sys.stdin.readline


def merge(lo: int, hi: int) -> None:
    if hi - lo > (N // k):
        return

    mid = (lo + hi) // 2
    left, right = lo, mid
    p = left
    while left < mid or right < hi:
        if left >= mid:
            temp[p] = chickens[right]
            right += 1
        elif right >= hi:
            temp[p] = chickens[left]
            left += 1
        elif chickens[left] <= chickens[right]:
            temp[p] = chickens[left]
            left += 1
        else:
            temp[p] = chickens[right]
            right += 1
        p += 1

    for i in range(lo, hi):
        chickens[i] = temp[i]


def partition(lo: int, hi: int) -> None:
    if lo + 1 == hi:
        return

    mid = (lo + hi) // 2
    partition(lo, mid)
    partition(mid, hi)
    merge(lo, hi)


N = int(input())
chickens = list(map(int, input().split()))
temp = [0] * N
k = int(input())

partition(0, N)
print(*chickens)