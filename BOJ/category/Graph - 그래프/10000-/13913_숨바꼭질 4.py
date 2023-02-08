import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e5)


def bfs(start, end) -> list:
    q = deque([start])
    visited = [-1] * (INF + 1)
    trace = [-1] * (INF + 1)
    visited[start] = 0

    while q:
        now = q.popleft()

        for nxt in [now - 1, now + 1, now * 2]:
            if nxt < 0 or nxt > INF or visited[nxt] != -1:
                continue
            visited[nxt] = visited[now] + 1
            trace[nxt] = now
            q.append(nxt)

        if visited[end] != -1:
            break

    return [visited[end]] + trace_route(trace, end, start)


def trace_route(trace, loc, start) -> list:
    rst = []
    while trace[loc] != -1:
        rst.append(loc)
        loc = trace[loc]

    rst.append(start)
    return rst[::-1]


start, end = map(int, input().split())
ans = bfs(start, end)
print(ans[0])
print(*ans[1:])

"""
13913. 숨바꼭질 4
    - 기본적인 그래프 탐색 그런데 이제 역추적을 곁들인

    - BFS로 탐색시에 이전 노드를 기록하는 trace[] 배열을 하나 두고 저장한 후에
      역추적으로 경로를 되찾아 가면 된다. 
"""