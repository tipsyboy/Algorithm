# 경로 압축 기법
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


v, e = map(int, input().split())  # node 갯수, 간선 개수(union 연산 수)
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False  # cycle check

for i in range(e):
    x, y = map(int, input().split())

    # 서로소 집합이 아니면 (둘이 같은 집합이면 == 같은 루트노드를 갖고 있으면)
    if find_parent(parent, x) == find_parent(parent, y):
        cycle = True
        break
    else:  # cycle이 발생하지 않았다면 union 연산
        union_parent(parent, x, y)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
