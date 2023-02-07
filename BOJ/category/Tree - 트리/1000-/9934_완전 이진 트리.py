import sys

input = sys.stdin.readline


def get_tree_by_inorder(lv, start, end) -> None:
    if start > end:
        return

    # 이번 서브트리에서의 root 값 찾기
    mid = (start + end) // 2
    graph[lv].append(inorder[mid])

    get_tree_by_inorder(lv + 1, start, mid - 1)  # left sub tree
    get_tree_by_inorder(lv + 1, mid + 1, end)  # right sub tree


K = int(input())
inorder = list(map(int, input().split()))
graph = [[] for _ in range(K)]
get_tree_by_inorder(0, 0, len(inorder) - 1)
for i in range(K):
    print(*graph[i])


"""
9934. 완전 이진 트리
    - 트리의 중위 순회(inorder traversal)이 주어졌을때, 원본 트리를 찾는 문제

    - 완전 이진 트리이므로 서브트리 t에 대해서 t의 index mid 값이 서브트리 t의 루트값이 된다.
      따라서 재귀로 서브트리를 좁혀 나가면서 해당 레벨의 루트 값들을 전부 찾아 나가면된다.
"""