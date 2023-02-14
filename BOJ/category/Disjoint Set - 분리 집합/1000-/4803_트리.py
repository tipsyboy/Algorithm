import sys

input = sys.stdin.readline


def find_parent(x: int, parent: list) -> int:
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)

    return parent[x]


def union_node(a: int, b: int, parent: list) -> None:
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


case = 1
while True:
    n, m = map(int, input().split())  # Node, Edge

    if n == 0 and m == 0:
        break

    parent = [0] * (n + 1)
    is_tree = [True] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    for _ in range(m):
        a, b = map(int, input().split())

        if find_parent(a, parent) != find_parent(b, parent):
            # 연결 이전에 사이클이 존재하는 경우
            is_tree[min(find_parent(a, parent), find_parent(b, parent))] = (
                is_tree[find_parent(a, parent)] & is_tree[find_parent(b, parent)]
            )
            union_node(a, b, parent)
            continue

        # 연결로 인해 사이클 발생
        is_tree[min(find_parent(a, parent), find_parent(b, parent))] = False

    trees = set()
    for i in range(1, n + 1):
        if is_tree[find_parent(i, parent)]:
            trees.add(find_parent(i, parent))

    if not trees:
        print("Case %d: No trees." % case)
    elif len(trees) == 1:
        print("Case %d: There is one tree." % case)
    else:
        print("Case %d: A forest of %d trees." % (case, len(trees)))
    case += 1
