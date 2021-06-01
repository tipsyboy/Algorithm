import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)  # 재귀 depth 늘리기


# 1) dfs
def dfs_algo():
    # 4방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # dfs
    def dfs(x, y, color):
        # graph 범위를 넘어서는 구간
        if x <= -1 or x >= n or y <= -1 or y >= n:
            return False

        # 아직 방문하지 않은 노드에서 색이 같으면 이전 노드와 같은 노드임.
        if graph[x][y] == color and not visited[x][y]:
            visited[x][y] = True  # 노드를 방문처리하고

            # 4방향 이동
            for i in range(4):
                dfs(x + dx[i], y + dy[i], color)

            return True  # return

        return False  # 위의 조건식에 걸리지 않으면 False

    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]  # graph
    visited = [[False] * n for _ in range(n)]
    rst = [0, 0]  # 적록색약이 아닌 사람 / 적록색약인 사람

    # 1) 적록색약이 아닌 사람
    for i in range(n):
        for j in range(n):
            if dfs(i, j, graph[i][j]):
                rst[0] += 1

    # 2) 적록색약인 사람
    # 변환
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "R":
                graph[i][j] = "G"
    visited = [[False] * n for _ in range(n)]  # visited list 초기화

    for i in range(n):
        for j in range(n):
            if dfs(i, j, graph[i][j]):
                rst[1] += 1

    print(rst[0], rst[1])


def bfs_algo():

    def bfs(start_x, start_y, color):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque([(start_x, start_y)])

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == color and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    rst = [0, 0]  # 적록색맹이 아닌 사람 / 적록색맹인 사람

    # 1) 적록색맹 x
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, graph[i][j])
                rst[0] += 1

    # 2) 적록색맹
    visited = [[False] * n for _ in range(n)]  # init visited list
    # 변환
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "R":
                graph[i][j] = "G"

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, graph[i][j])
                rst[1] += 1

    print(rst[0], rst[1])


# dfs_algo()
bfs_algo()

"""
46. 10026 적록색약 (Gold 5)
    - 완전 탐색문제로 dfs/bfs로 각각 해결했다. 검색해보니까 bfs로 해결한 사람이 더 많던데,
      동빈나 책의 영향인지 아이스크림 얼려먹기 같은 문제는 dfs를 먼저 떠올리게 된다. 
      코드는 금방 짰는데, 런타임 에러가 떠서 문제 찾던 도중에 python recursion limit 때문임을 알게 되었다.
    
    - python에서는 재귀 depth 제한이 있기 때문에 dfs를 사용하거나 기타 재귀문을 사용할 때,
      주의해서 sys.setrecursionlimit(limit)를 써준다.
    
    - 이전의 연습했던 문제들과 사~알짝 다른 점은 
      이전의 문제들은 길을 갈 수 있는 곳 / 없는 곳(범위를 벗어나는 것 포함)이 전부였으나, 
      이번 문제는 RGB 색에 따라서 구역을 나눠서 갖는 것이었다. 
      매개변수를 추가해 color 정보를 함수에 전달하면서 문제를 해결했다. 
"""
