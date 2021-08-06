import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(0, 0, 1)])
    # visited = [[[0] * 2] * m for _ in range(n)] # 얕은 복사 이슈
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while q:
        x, y, chance = q.popleft()

        # 목적지에 도달한 경우
        if x == n - 1 and y == m - 1:
            return visited[x][y][chance]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 가려는 좌표에 벽이 있는 경우 - 벽을 부술 수 있는 찬스가 있어야 진행 가능
                if graph[nx][ny] == 1 and chance == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append((nx, ny, 0))
                # 벽이 없는 경우 - 가려는 곳이 방문하지 않은 곳이어야 함
                elif graph[nx][ny] == 0 and not visited[nx][ny][chance]:
                    visited[nx][ny][chance] = visited[x][y][chance] + 1
                    q.append((nx, ny, chance))

    return -1


n, m = map(int, input().split())
graph = [list(map(int, str(input().rstrip()))) for _ in range(n)]

print(bfs())


"""
35. 2206 벽 부수고 이동하기 (Gold 4)
    1. 
    - 그냥 bfs에다가 예전에 치킨거리인가 그 문제랑 같은거라고 생각해서 
      graph 받을때, 모든 벽의 위치를 저장했다가 벽을 하나씩 지웠다가 복구하면서, bfs를 돌렸다. 
    
    - TLE 받음... 이제 그냥 완전 단순한 bfs는 안나오는것 같다. 

    2.
    - 3차원 배열을 사용해서 부술수 있는 횟수를 z축에 저장했다.
      visited[row][col][chance]는 chance 횟수에서 (x, y)에 도달했을 때의 최단거리를 얘기하는 것이다. 

    - 이후에 이동하려고 하는 좌표 (nx, ny)에서 벽이 있는지/없는지만 구분해서 bfs를 돌려주면 된다. 

    3. 
    - 3차원 배열을 사용하는 것이 아직 익숙하지가 않다. 

    - visited[]를 선언하고 사용할때, 얕은복사 이슈가 있었다.
      찾는데 한참 걸렸는데, 아직도 좀 헷갈린다.
"""
