# https://www.acmicpc.net/problem/2611

import sys
from collections import deque

input = sys.stdin.readline


def get_route(cur: int, end: int, prev: list) -> list:
    route = [cur]

    while prev[cur] != end:
        route.append(prev[cur])
        cur = prev[cur]

    route.append(prev[cur])
    return route


def t_sort(start: int) -> list:
    q = deque([(start, 0)])

    prev = [0] * (N + 1)
    scores = [0] * (N + 1)
    while q:
        cur, total_now = q.popleft()

        if cur == start and total_now != 0:
            break

        for adj, score in graph[cur]:
            indegree[adj] -= 1

            if scores[adj] < total_now + score:
                scores[adj] = total_now + score
                prev[adj] = cur

            if indegree[adj] == 0:
                q.append((adj, scores[adj]))

    ans = get_route(1, 1, prev)
    ans.append(scores[1])
    return ans


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    indegree[q] += 1

ans = t_sort(1)
print(ans.pop())
print(" ".join(map(str, ans[::-1])))

"""
2611. 자동차경주
    - 처음엔 위상 정렬로 해결해야 한다는 생각은 했으나, 
      갈때/올때를 나눠서 두 번에 걸쳐서 위상 정렬을 수행했고, 코드가 꼬이기 시작하면서 WA

    - 문제를 잘 읽어야 한다..
    - 1) "단, 중간에는 1번 지점을 지나서는 안 된다. 
          경주로는 1번 지점을 제외한 어느 지점에서 출발하여도 1번 지점을 지나가지 않고서는 같은 지점으로 돌아올 수 없도록 되어 있다."
         -> 1번 노드를 제외한 임의의 노드 x는 1번 노드를 거치지 않고는 다시 x로 돌아올 수 없다. 
           -> x로 돌아가려면 1을 무조건 거쳐야한다.
             -> 1번노드에서 1번노드로의 사이클은 존재하나, 다른 점들끼리는 사이클이 존재하지 않는다.
               -> 때문에 여타 다른 문제와 같이 위상 정렬을 수행하고 돌아서 1번 노드로 돌아왔을때, 종료 해준다.

      2) "또한 1번 지점에서 다른 모든 지점으로 갈 수 있고, 다른 모든 지점에서 1번 지점으로 갈 수 있다."
         -> 그래프는 모두 연결되어 있다.
           -> 위상 정렬이 가능하다.
"""