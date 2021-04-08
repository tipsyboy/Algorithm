
# 기존의 방법
def find_parent_basic(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])

    return x

# 경로 압축 기법


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    # 두 노드의 비교 결과 더 작은 노드의 parent가 parent가 된다.
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


# 노드, 간선 입력
v, e = map(int, input().split())  # 노드 갯수, 간선 갯수(Union 연산 수)
parent = [0] * (v+1)  # 부모 노드 테이블 초기화

# 부모노드 테이블 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


# union 연산을 수행
for i in range(e):
    x, y = map(int, input().split())
    union_parent(parent, x, y)

print("각 원소가 속한 집합: ", end="")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")
print()
print("부모 테이블: ", end="")
for i in range(1, v+1):
    print(parent[i], end=" ")


# 경로 압축 기법을 사용했을 때, find_parent() 한번 걸쳐야 전체 노드를 털면서 자신 x의 부모 노드를 찾을 수 있다.
# 이때 이미 조사는 다함 -> 다음에 사용할 때 부터 시간 복잡도가 개선되는 것
