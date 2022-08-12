# https://www.acmicpc.net/problem/3273
# 2022-08-12 Fri

import sys

input = sys.stdin.readline
MAXV = 1_000_000


def two_pointer(N: int, arr: list, x: int) -> int:
    sorted_arr = sorted(arr)

    left, right = 0, N - 1
    cnt = 0
    while left < right:
        sumv = sorted_arr[left] + sorted_arr[right]

        if sumv > x:
            right -= 1
        elif sumv < x:
            left += 1
        else:
            cnt += 1
            # 원소는 서로 다른 수
            right -= 1
            left += 1

    return cnt


def arr_solution(N: int, arr: list, x: int) -> int:
    nums = [False] * (MAXV + 1)
    for elem in arr:
        nums[elem] = True

    right = x // 2 if x % 2 == 0 else x // 2 + 1
    cnt = 0
    for i in range(1, right):
        if x - i > MAXV:
            continue
        if nums[i] and nums[x - i]:
            cnt += 1

    return cnt


N = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(arr_solution(N, arr, x))
print(two_pointer(N, arr, x))


"""
3273. 두 수의 합
    - 주어진 수열에서 두 수의 합이 x가 되는 순서쌍 (p, q)를 구하는 문제

    - 처음에 투 포인터로 해결했지만, 단순 배열로도 해결할 수 있다. 
"""