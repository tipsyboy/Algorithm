import sys

input = sys.stdin.readline


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


n = int(input())  # 초기 동방의 개수
m = int(input())  # 빅-종빈빌런의 행동 횟수

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    x, y = map(int, input().split())

    for i in range(x, y):
        union_parent(parent, i, i + 1)


#
for i in range(1, n + 1):
    find_parent(parent, i)

rst = set()
for p in parent[1:]:
    if p not in rst:
        rst.add(p)

print(len(rst))


"""
14594. 동방 프로젝트 (small) (Silver 3)
    - 빅-종빈빌런이 벽을 부술때, 입력 값이 sorting되서 들어오는 것은 아니기 때문에 마지막에
      모든 노드에 대해서 find_parent()를 한번 더 실행해준다. 

      이 과정이 없어서 처음에 WA를 받았다. 
"""
