import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(start_x, start_y)])
    visited = [[False] * m for _ in range(n)]
    visited[start_x][start_y] = True
    remove_cheese = set()

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 다음 좌표가 치즈인 경우
                if graph[nx][ny] != 0:
                    graph[nx][ny] += 1

                    # 공기와 접촉을 2번 이상 (원래 1이므로 3이상)
                    if graph[nx][ny] >= 3:
                        remove_cheese.add((nx, ny))
                # 다음 좌표가 공기
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))  # 방문처리 후 큐에 추가

    return remove_cheese


n, m = map(int, input().split())
cheese = set()  # 치즈
graph = []

# 입력 및 치즈 위치
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(m):
        if temp[j] == 1:
            cheese.add((i, j))

    graph.append(temp)


time = 0  # 지난 시간
while True:
    # cheese가 없다면
    if not cheese:
        break

    # 제거할 치즈 구해와서 치즈 제거
    remove_cheese = bfs(0, 0)
    cheese = cheese - remove_cheese

    for x, y in remove_cheese:
        graph[x][y] = 0

    # 공기가 2번 이상 닿지 않은 치즈들 초기화
    for x, y in cheese:
        graph[x][y] = 1

    time += 1

print(time)


"""
37. 2638 치즈 (Gold 4)
    1.
    - 외부 공기에 치즈가 닿은 횟수를 찾는 탐색문제 bfs라고 생각했고, 문제가 있었다. 
      1) 닿는 부분이 외부공기인 것은 어떻게 판단할 것인가?
    
    2. 
    - 치즈를 대상으로 탐색을 시작하는 것이 아니고 공기를 중심으로 탐색해야 한다고 생각하게 됨.
    
    - 외부 공기인것을 판단하기 위해서 (0, 0)부터 시작해서 (문제에서 가장자리에는 치즈가 놓이지 않는다고 가정한다.) 
      1) 공기들을 중심으로 탐색하고, 
      2) 이때 next_position을 결정할때 만약 치즈라면 queue에 넣지 않는 방법을 택한다. 
      3) 위와 같이 탐색하면 무조건 외부공기인 (0, 0)에서 출발하기 때문에 치즈를 뚫고 들어가서 탐색하지 않게 된다. 
      4) 따라서 외부 공기만 탐색하면서 닿는 치즈의 위치에 +=1을 해주면서 공기에 닿는 부분을 탐색할 수 있게된다. 

    - visited나 방문횟수 이외에도 queue에 넣는 조건을 제한함으로써, 탐색 범위를 결정할 수 있다. 

    3.
    - 처음에는 
      1) 제거할 치즈를 찾는 bfs()
      2) 현재 그래프에 치즈가 남았는지 확인하는 함수 
      3) 치즈를 제거하는 함수 
    
      이렇게 셋을 두어서 분할해서 풀이하려고 했는데, set()을 활용해서 좌표를 저장하면 시간복잡도를 줄일 수 있을 것 같아서 위의 코드를 그렇게 구현했다. 
      꽤 많이 차이날 것으로 생각하고 이렇게 풀었는데, BOJ 채점 결과 별로 큰 차이는 없었다. (100ms 정도?)
      AC 받
"""