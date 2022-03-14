# 위상 정렬(Topology Sort)
from collections import deque

# 노드의 개수와 간선 수 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수를 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 그래프 초기화 (인접리스트)
graph = [[] for i in range(v + 1)]

# 간선 정보를 입력 받는다.
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # node A -> node B

    indegree[b] += 1  # 진입 차수 1 증가


# 위상 정렬 함수
def topology_sort():
    result = []  # 결과 값을 담을 리스트 (큐에서 노드가 빠져나감을 정리)
    q = deque()  # 큐 정의

    # 처음에는 진입차수가 0인 노드만 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌때까지 반복한다.
    while q:
        # 원소 꺼내기
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1  # 진입차수 하나 내림
            # 새롭게 진입 차수가 0이 되면 큐에 추가
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")


topology_sort()

"""
test case
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""