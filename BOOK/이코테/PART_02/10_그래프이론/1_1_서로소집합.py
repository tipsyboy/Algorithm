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


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


#
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블을 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 진행한다.
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합을 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")
print()

# 부모 테이블의 내용 출력
print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")
print()


"""
1_1 서로소 집합(Disjoint Set)과 서로소 집합 자료구조
    - union-find 연산이라고도 하며 graph의 연결성을 집합의 형태로 파악하는데 사용할 수 있다. 
    1) 부모 노드 테이블을 따로 설정한 후, 노드는 초기에 자기 자신을 부모노드로 갖는다. 
    2) Node의 연결 상태를 통해서 각 노드의 부모노드를 find 연산으로 찾고, union 연산을 통해서 연결성을 갖는 노드를 연결한다. 
       이때, 문제의 조건에 따라서 부모노드가 설정되지만, 언급이 없는 경우 관행적으로 더 낮은 번호의 노드가 부모노드가 된다. 
    3) 2)를 반복한다. 

    - 기본적인 서로소 집합 알고리즘
      기본적으로 union을 진행하면서 parent 테이블이 갱신되는데, find를 통해서 union으로 결합을 통해 찾은 부모노드를 찾아가는 방법이다. 

    - 경로 압축 기법을 통한 서로소 집합
      위의 기본적인 방법의 경우 연속적으로 연결된 부모노드를 계속 찾아나가기 때문에 최악경우 시간복잡도에서 상당한 손해를 볼 수 있다. 
      때문에 경로 압축 기법은 부모 노드를 찾아가는 과정에서 계속해서 부모노드 갱신을 집합의 root노드로 갱신한다.
      
      이 방법을 통해서 노드의 최종 부모노드가 무엇인지 바로 알 수 있게된다. 
"""