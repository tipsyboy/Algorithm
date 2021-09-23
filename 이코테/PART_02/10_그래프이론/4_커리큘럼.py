import sys
from collections import deque

input = sys.stdin.readline


def topological_sort(n, graph, time, indegree):
    # time과 별개의 rst 리스트
    rst = [0] * (n + 1)
    for i in range(1, n + 1):
        rst[i] = time[i]

    # 진입 차수가 0인 노드를 큐에 추가
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            # 진입 차수 하나씩 줄여주고
            indegree[i] -= 1
            rst[i] = max(rst[i], rst[now] + time[i])  # *****

            if indegree[i] == 0:
                q.append(i)

    for i in rst:
        print(i)


n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))

    time[i] = data[0]  # 이 강의를 수강하는데 드는 시간
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

topological_sort(n, graph, time, indegree)


"""
4_ 커리큘럼 
    - 위상정렬 문제

    - 예시가 이해가 잘 안됐었는데, '동시에 여러강의를 들을 수 있다'라는 문장을 빼놓고 읽었었다. 
      같은 이유로 rst를 계산하는 방법을 수행하는데, max값을 사용하는 이유가 now강의의 다음 강의를 듣기 위해서
      이전 강의의 모든 요구조건을 완성하고 와야하지만 동시에 들을 수 있기 때문에 누적합이 아닌 max값으로 갱신해 주는 것이다. 

"""