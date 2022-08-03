import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float("inf")
directions = [(-1, 0), (1, 0), (0, 1)]


def dijkstra() -> int:
    pq = []
    visited = [[INF] * M for _ in range(N)]

    for i in range(N):
        if graph[i][0] == 0:
            heappush(pq, (0, i, 0))
            visited[i][0] = 0

    while pq:
        handle, x, y = heappop(pq)

        if handle > visited[x][y]:
            continue

        if y == M - 1:
            return handle

        for i in range(3):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] == 1:
                continue

            nxt_handle = handle if i == 2 else handle + 1
            if visited[nx][ny] > nxt_handle:
                heappush(pq, (nxt_handle, nx, ny))
                visited[nx][ny] = nxt_handle

    return INF


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = dijkstra()
if ans == INF:
    print("NIE")
else:
    print(ans)


"""
8687. Pasy Ruchu
    0. 
    - 처음에 자바로 하다가 계속 MLE가 뜨길래 언어 문제인가 싶어서 파이썬으로 풀었는데,
      TLE가 떠서 이것 저것 처리 이후에 통과했다. 정해는 아니고 어찌어찌 뚫은 것.
      결론적으로 같은 방식으로 했을 때, 파이썬으로는 통과 pq에 Node를 넣느냐 튜플을 넣느냐 방식차이로 MLE를 피하고
      더 이상 탐색할 수 없는(필요가 없는) 경우를 제외해줌으로 TLE를 피해서 뚫음
    
    1. 문제가 물어보는 것
    - 주어진 그래프의 0열에서 M-1열까지 이동할 때, 꺾는 횟수를 최소화 하는 문제
    
    1-1. 포인트 ?
    - 어찌 어찌 뚫은 이후에 다른 사람들의 풀이를 보니 0열의 i번째를 출발 지점으로 두고 시작하는 것이 아닌
      0열의 모든 출발 가능한 점을 pq에 넣고 시작했다. 
    
      생각해보니 출발 지점끼리의 이동은 [차선 변경 횟수+1]로 시작하는 것이므로 이미 최적해가 아니게 된다. 
      따라서, 모든 0열의 노드에서 출발하는 것이 아닌 출발 가능한 모든 0열의 노드를 전부 pq에 넣고 출발한다. 
    
    2. 필요 알고리즘 개념
    - 그래프 이론, 다익스트라 알고리즘, 0-1 BFS(미풀이)
    
    3. 풀이 이후
    - 0-1 BFS로도 해결이 가능하다고 하나, 아직 익숙하지 않기 때문에 개념 공부 이후에 다시 해결해볼 것
"""