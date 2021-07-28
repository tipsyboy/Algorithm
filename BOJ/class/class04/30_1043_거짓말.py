import sys
from collections import deque
input = sys.stdin.readline


# 1) 브루트포스?
def solution1():
    # 1. 입력 값
    n, m = map(int, input().split())  # 사람 / 파티 수
    init_witness = list(map(int, input().split()))
    witness = set(init_witness[1:])
    party_list = []  # party

    # input party guest list
    for _ in range(m):
        party = list(map(int, input().split()))
        party_list.append(party)

    # 2. 진실을 아는 사람이 하나도 없는 경우
    if init_witness[0] == 0:
        return m

    # 3. 파티를 모두 확인하면서 진실을 아는 사람 전파
    for _ in range(m):
        for party in party_list:
            if witness.intersection(set(party[1:])):
                witness.update(party[1:])

    # 4. 파티를 모두 확인 하면서 거짓말 할 수 있는 횟수 카운팅
    count = 0
    for party in party_list:
        if not (witness.intersection(set(party[1:]))):
            count += 1

    return count


# 2) union-find
def solution2():

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])

        return parent[x]

    def union_parent(parent, a, b):
        # list로 한꺼번에 하다가 변경했다.
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    # 1. input data
    n, m = map(int, input().split())
    init_witness = list(map(int, input().split()))

    # parent 선언 및 초기화
    parent = [0] * (n + 1)
    for i in range(1, n+1):
        parent[i] = i

    # 2. party 내용 받고 노드들 union
    party_list = []
    for _ in range(m):
        guest = list(map(int, input().split()))[1:]

        for i in range(len(guest) - 1):
            a = guest[i]
            b = guest[i + 1]
            union_parent(parent, a, b)

        party_list.append(guest)

    # 3. 사실을 알고 있는 사람이 하나도 없는 경우
    if init_witness[0] == 0:
        return m

    # 4. 거짓말을 못하는 횟수 카운팅
    count = 0
    for party in party_list:
        for witness in init_witness[1:]:
            # 여기가 좀 헷갈렸다.
            # 노드의 연결관계를 판단해서 집합관계를 찾는 것이므로 당연히 find과정이 한번 더 있다.
            if find_parent(parent, party[0]) == find_parent(parent, witness):
                count += 1
                break  # 한 명이라도 진실을 알고 있는 경우 거짓말을 못치므로 break

    return m - count


# 3. bfs로 풀기
def solution3():
    def bfs(start):
        q = deque([start])
        visited[start] = True

        while q:
            now = q.popleft()

            for nxt in graph[now]:
                if not visited[nxt]:
                    q.append(nxt)
                    visited[nxt] = True
                    init_witness.append(nxt)

    # 1. 입력 받기
    n, m = map(int, input().split())
    init_witness = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    # 2. 입력 받기 및 graph 설정
    party_list = []
    for _ in range(m):
        guest = list(map(int, input().split()))[1:]

        for i in range(len(guest) - 1):
            for j in range(i + 1, len(guest)):
                graph[guest[i]].append(guest[j])
                graph[guest[j]].append(guest[i])

        party_list.append(guest)

    # 3.
    if init_witness[0] == 0:
        return m
    init_witness = init_witness[1:]

    # 4.
    for i in init_witness:
        if not visited[i]:
            bfs(i)

    # 5.
    count = 0
    for party in party_list:
        if not set(party).intersection(set(init_witness)):
            count += 1

    return count


# print(solution1())
# print(solution2())
# print(solution3())


# 6 5
# 1 6
# 2 4 5
# 2 1 2
# 2 2 3
# 2 3 4
# 2 5 6
# 답 0

# 4 5
# 1 1
# 1 1
# 1 2
# 1 3
# 2 4 2
# 2 4 1
# 답 1

"""
30. 1043 거짓말 (Gold 4)
    - 굉장히 골머리 앓았던 문제... 현재 기준 class04 gold5 -> gold4로 넘어가는 문제였는데, 
      벽이 느껴질정도로 하루 꼬박사용해서 풀었는데 풀고나니까 크게 어려운거 같지도 않고 모르겠다. 
      테스트 케이스 다 통과하고 나서도 계속 틀렸렸고, 반례를 못찾았었다. 아무튼 이거 하느라 머리 너무 아픔. 
    
    - 문제는 파티가 열린 순서는 정해져 있지 않고, 진실을 알고 있는 사람이 한명이라도 있으면, 소문이 퍼져나간다. 
      때문에 모든 파티를 전부 검사하면서 진실을 알고 있는 인원을 늘려나가야 한다. 

    - 당연히 진실을 알고 있는 인원이 하나도 없는 경우 파티의 숫자만큼 지민이는 거짓말을 할 수 있다. 

    1. 브루트포스 ?
    - 모든 파티를 전부 입력 받은 이후에 파티를 전부 점검하면서 진실을 알고 있는 사람들을 확장 시켜나가고
      모든 파티를 전부 점검한 이후에, 다시 파티리스트를 돌면서 거짓말을 할 수 있는 횟수를 다시 센다. 
    
    - 모든 파티리스트를 계속 돌면서 witness를 늘려 나가기 때문에 처음에는 매우 꺼려졌던 문제였는데, 
      다른 생각이 안나서 + 범위가 작아서 이걸로 제출했다. 여유있게 AC받음

    - python set() 메소드의 교집합/합집합에 대해서 공부했고, set()의 다수 원소 확장으로 update()에 대해서 알게됨. 

    2. find-union (서로소 집합, Disjoint set)
    - 사실 이걸로 푸느라고 머리 터질뻔함. 

    - union-find의 경우에는 find_parent()의 목적이 "루트 노드를 찾는 행위" 라는 것에 중점적으로 생각하면서 풀이해야한다. 
      처음에 굉장히 많이 틀렸던 이유도 루트 노드를 찾아서 노드간의 연결을 파헤치는게 아니고 단순히 
      현재 union 되려는 노드들의 부모만 찾아 나갔지 때문에 틀렸었다.(말이 굉장히 애매모호해서 다음에 보면 모를 수도 있겠다.)
      union하는 과정에서 party의 리스트가 단독으로 2개를 연결하지 않고, 리스트 형태로 한번에 연결하려다 보니 
      중복되는 것에 대해서 생각하지 않았고, 때문에 루트 노드를 찾는 것이 아닌 당시에 작은 노드가 부모노드가 되는 경우가 생겨서 매우 많이 틀렸었다. 

      나중에 리스트 형태로 한번에 하지 않고 그냥 반복문을 통해서 2개 노드씩 연결하는 것이 더 좋다는 판단되었다. 

    - 쨌든, 코드에서는 각 노드들을 union-find를 통해서 모든 노드들의 연결관계를 찾았으므로, 
      파티 게스트 0번과 모든 진실을 알고 있는 사람의 부모노드를 비교한다. 

    3. bfs()
    - 이것도 완전탐색이니까 브루트포스의 한 종류라고 생각할 수도 있는데, 따로 분류한다. 

    - 코드에서는 모든 파티의 내용을 graph로 입력을 받고 bfs()로 탐색하면서 서로의 연결관계에서
      진실을 알고 있는 사람의 수를 늘려나간다. 
    
    - 이후 1번 풀이와 같이 진실을 알고 있는 사람과 파티의 사람들 사이의 교집합을 찾아내서 지민이가 거짓말을 할 수 있는 횟수를 카운팅 한다. 

"""
