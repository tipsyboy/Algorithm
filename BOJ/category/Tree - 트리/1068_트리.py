import sys

input = sys.stdin.readline


def dfs(node: int) -> int:
    global cnt

    if visited[node]:
        return

    visited[node] = True
    if not tree[node]:
        cnt += 1
        return

    for child in tree[node]:
        dfs(child)


N = int(input())
arr = list(map(int, input().split()))
deleted_node = int(input())
root = -1

tree = [[] for _ in range(N)]
for i in range(N):
    if i == deleted_node:
        continue

    if arr[i] == -1:
        root = i
        continue

    tree[arr[i]].append(i)


visited = [False] * N
cnt = 0
if root != -1:
    dfs(root)
print(cnt)


"""
1068. 트리
    - 트리에서 임의의 노드와 그 자식들을 지웠을 때, 
      리프 노드의 개수를 세는 문제

    - root가 지워진 경우 or 자식 노드가 삭제 되어서 자신이 리프 노드가 되는 경우를 잘 생각해야 한다. 
"""