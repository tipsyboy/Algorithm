# 경로 압축 기법
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = map(int, input().split())  # node 갯수, 간선 개수(union 연산 수)
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i


cycle = False  # cycle check
for i in range(e):
    a, b = map(int, input().split())

    # 유니온 이전에 이미 연결되어 있다는 뜻이니 사이클이 발생했다고 볼 수 있다.
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:  # cycle이 발생하지 않았다면 union 연산
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
