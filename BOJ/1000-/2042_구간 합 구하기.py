import sys
from math import ceil, log2

input = sys.stdin.readline


def init_tree(start: int, end: int, node: int) -> int:
    # node: 이번 node 번호, start: 이번 node의 시작, end: 이번 node의 끝점
    if start == end:  # leaf node
        tree[node] = arr[start]
        return tree[node]

    # leaf node가 아닌 경우 mid를 기준으로 구간을 나눈다.
    mid = (start + end) // 2
    # 이번 node의 left 자식 노드 번호 node*2, 이번 node의 right 자식 노드 번호 node*2 + 1
    tree[node] = init_tree(start, mid, node * 2) + init_tree(mid + 1, end, node * 2 + 1)
    return tree[node]


def update_tree(start: int, end: int, node: int, target: int, val: int) -> None:
    # target: 기존 배열에서 값이 변경된 index 즉 target_index, val: 변경된 값

    # 1) 범위를 벗어난 경우 업데이트 할 필요가 없음
    if target < start or target > end:
        return

    # 2) leaf node에 도달했을 때, 값을 변경한다.
    if start == end and start == target:
        tree[node] = val
        return

    # 3) 위의 경우가 아닐때, mid 값을 기준으로 세그트리를 탐색해 나간다.
    mid = (start + end) // 2
    update_tree(start, mid, node * 2, target, val)
    update_tree(mid + 1, end, node * 2 + 1, target, val)

    # 4) 자식 노드에서 갱신된 값을 가지고 현재 노드를 갱신
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start: int, end: int, node: int, left: int, right: int) -> int:
    # 세그 트리의 구간을 벗어남
    if end < left or start > right:
        return 0

    # 현재 구간이 내가 구하고 싶은 구긴에 포함된다.
    if start >= left and end <= right:
        return tree[node]

    # 위의 경우가 아닐때, mid를 중심으로 다시 탐색
    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)


N, M, K = map(int, input().split())  # 수의 개수, 업데이트, 쿼리
arr = []
for _ in range(N):
    arr.append(int(input()))

lv = int(ceil(log2(N)))
tree = [0] * (1 << (lv + 1))

init_tree(0, N - 1, 1)
for _ in range(M + K):
    com, b, c = map(int, input().split())
    if com == 1:
        update_tree(0, N - 1, 1, b - 1, c)
    elif com == 2:
        print(query(0, N - 1, 1, b - 1, c - 1))


"""
2042. 구간 합 구하기
    - 세그먼트 트리 가장 기초 문제 
"""