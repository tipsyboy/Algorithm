# https://www.acmicpc.net/problem/1991

import sys

input = sys.stdin.readline


def preorder(cur: int) -> None:
    # root -> left -> right

    print(chr(cur + 64), end="")

    if left[cur] != -1:
        preorder(left[cur])

    if right[cur] != -1:
        preorder(right[cur])


def inorder(cur: int) -> None:
    # left -> root -> right

    if left[cur] != -1:
        inorder(left[cur])

    print(chr(cur + 64), end="")

    if right[cur] != -1:
        inorder(right[cur])


def postorder(cur: int) -> None:
    # left -> right -> root
    
    if left[cur] != -1:
        postorder(left[cur])

    if right[cur] != -1:
        postorder(right[cur])

    print(chr(cur + 64), end="")


N = int(input())
left = [-1] * (N + 1)
right = [-1] * (N + 1)
for _ in range(N):
    root, l, r = map(lambda x: ord(x) - 64, input().split())

    left[root] = l if l != -18 else -1
    right[root] = r if r != -18 else -1


preorder(1)
print()
inorder(1)
print()
postorder(1)