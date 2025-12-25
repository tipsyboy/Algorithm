# https://www.acmicpc.net/problem/23883
# 2022-08-10 WED

import sys

input = sys.stdin.readline


def selection_sort(arr: list, N: int, K: int) -> list:
    pq = []
    idx_dict = dict()
    for i in range(N):
        idx_dict[arr[i]] = i

    maxv_list = sorted(arr)
    cnt = 0
    for i in range(N - 1, 0, -1):
        maxv = maxv_list[i]
        if maxv > arr[i]:
            now_val = arr[i]
            arr[i], arr[idx_dict[maxv]] = arr[idx_dict[maxv]], arr[i]
            idx_dict[now_val], idx_dict[maxv] = idx_dict[maxv], idx_dict[now_val]
            cnt += 1

        if cnt == K:
            return arr

    return [-1]


N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(*selection_sort(arr, N, K))


"""
23883. 알고리즘 수업 - 선택 정렬3
    - 선택 정렬의 교환 순서를 알기 위해 정렬을 해야하는...

    - 오름차순 선택정렬은 뒤에서 부터 매번 자리마다 가장 큰 값을 선택해서 바꿔주는 정렬로
      nlogn 정렬을 통해서 이번 차례에 들어갈 가장 큰 값을 선택하고
      dict()를 활용해 이전 위치를 저장해가면서 선택정렬을 사용하면 된다. 
"""