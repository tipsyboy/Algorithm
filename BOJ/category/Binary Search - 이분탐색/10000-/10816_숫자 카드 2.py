# https://www.acmicpc.net/problem/10816

import sys
from collections import Counter
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def sol1_counter_module() -> list:
    count_arr = Counter(arr)

    rst = []
    for target in target_arr:
        rst.append(count_arr[target])

    return rst


def sol2_bisect_module() -> list:
    arr.sort()

    rst = []
    for target in target_arr:
        rst.append(bisect_right(arr, target) - bisect_left(arr, target))

    return rst


def sol3_dict() -> list:
    arr.sort()

    couter = dict()
    for e in arr:
        couter[e] = couter.get(e, 0) + 1

    rst = []
    for target in target_arr:
        if target in couter:
            rst.append(couter[target])
        else:
            rst.append(0)

    return rst


def sol4_binary_search() -> list:
    def left_idx(t: int, arr: list) -> int:
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo + hi) // 2

            if arr[mid] >= t:
                hi = mid
            else:
                lo = mid + 1

        return lo

    def right_idx(t: int, arr: list) -> int:
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo + hi) // 2

            if arr[mid] > t:
                hi = mid
            else:
                lo = mid + 1

        return lo

    arr.sort()
    rst = []
    for target in target_arr:
        rst.append(right_idx(target, arr) - left_idx(target, arr))

    return rst


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
target_arr = list(map(int, input().split()))

# print(*sol1_counter_module())
# print(*sol2_bisect_module())
# print(*sol3_dict())
print(*sol4_binary_search())

"""
10816. 숫자 카드 2
    - 모듈 사용(Counter, bisect), dict 사용, binary_search 직접 구현 4가지 방법으로 품

    - 4번을 구현할 수 있으면서 bisect를 사용하자
"""