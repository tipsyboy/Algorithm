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
edges = []  # 모든 간선을 담을 리스트
result_edges = []
result = 0  # 최종 비용을 담을 변수 ==> all cost

# 부모 테이블 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선의 내용을 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 간선들을 cost 오름차순 순으로 정렬하기 위해서 cost를 제일 앞

# cost 오름차순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result_edges.append((a, b))
        result += cost

print(result)
print(result_edges)  # 최소 신장트리 연결 간선들


# # 연결은 됐지만 찾기 전이라 parent table이 이전 부모 노드를 가리키고 있을 수도 있다. -
# print(parent)
# find_parent(parent, 4)
# print(parent)
# find_parent(parent, 7)
# print(parent)

# # test case
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
