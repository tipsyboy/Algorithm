
# 1)
# import sys
# from collections import deque
# input = sys.stdin.readline
# INF = int(1e9)


# # 현재 아기 상어의 위치에서 이동할 수 있는 모든 좌표의 거리 값을 계산하는 함수
# def cal_dist(start_x, start_y):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     dist = [[-1] * n for _ in range(n)]  # 거리 값 배열

#     q = deque([(start_x, start_y)])  # 현재 위치 queue에 저장
#     dist[start_x][start_y] = 0  # 현재 위치 이동 값 0

#     while q:
#         x, y = q.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # map을 벗어나지 않으면서 방문 하지 않은 구역에서
#             if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
#                 if graph[nx][ny] <= shark_size:  # 아기 상어의 크기보다 물고기의 크기가 작거나 같으면,
#                     q.append((nx, ny))  # 이동 가능
#                     dist[nx][ny] = dist[x][y] + 1

#     return dist


# # cal_dist() 함수 결과와 문제의 조건에 맞는 먹을 수 있는 물고기 찾으러 가기
# def find_fish(dist):
#     # 문제의 조건에 따라서 같은 거리라면 위쪽(row가 작은), 그래도 같다면 왼쪽(col이 작은)
#     # 물고기를 선택해야 한다. 기존의 방식대로 i-j 행렬 탐색하면 이 조건의 순서대로
#     # 공간을 탐색하기 때문에 따로 sorting 없이 진행해도 괜찮다.

#     x, y = 0, 0
#     min_dist = INF  # 먹을 수 있는 물고기 까지의 최소 거리 - 무한으로 초기화 한다.
#     for i in range(n):
#         for j in range(n):
#             if dist[i][j] != -1 and graph[i][j] != 0 and graph[i][j] < shark_size:  # 먹을 수 있는 물고기 중에서
#                 # 현재 위치보다 가까운 거리면 - 이전의 좌표가 위/왼쪽을 먼저 탐색하기 때문에 작은 경우에만 바꿈
#                 if dist[i][j] < min_dist:
#                     x, y = i, j
#                     min_dist = dist[i][j]

#     return (min_dist, x, y)  # 거리 최소 값, 좌표 리턴


# n = int(input())  # 맵의 크기 (n x n)
# graph = []  # map 입력 받기
# for i in range(n):
#     temp = list(map(int, input().split()))

#     for j in range(n):
#         if temp[j] == 9:  # 아기상어의 초기 위치를 저장하기 위함.
#             shark_x, shark_y = i, j
#             temp[j] = 0  # 상어의 위치는 아무것도 없는 것으로

#     graph.append(temp)

# shark_size = 2  # 아기 상어의 최초 크기
# eat_fish = 0  # 현재 크기에서 먹은 물고기의 수
# rst = 0  # 결과 시간 값

# # 물고기 탐색을 시작
# while True:
#     dist = cal_dist(shark_x, shark_y)
#     # print(dist)
#     time, x, y = find_fish(dist)  # 물고기를 찾는다.

#     # 리턴받은 시간이 무한대인 경우
#     if time == INF:
#         print(rst)  # 더 이상 먹을 물고기가 없는 경우이므로 종료한다.
#         break
#     else:  # 먹을 물고기를 찾음
#         shark_x, shark_y = x, y  # 상어의 위치 이동
#         graph[x][y] = 0  # 먹고
#         eat_fish += 1  # 먹은 물고기 수 증가
#         rst += time  # 먹으러 간 시간 추가

#         if eat_fish == shark_size:  # 상어의 크기가 증가하는 경우
#             shark_size += 1
#             eat_fish = 0


# 2) 단일 bfs()로 처리하기
import sys
from collections import deque
input = sys.stdin.readline


def find_fish(shark_x, shark_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(shark_x, shark_y)])
    visited = set((shark_x, shark_y))

    shark_size = 2
    eat_fish = 0
    flag = False  # 이중 loop 탈출
    time = 0
    rst = 0

    while q:
        length = len(q)

        q = deque(sorted(q))
        # print(q)
        for _ in range(length):
            x, y = q.popleft()

            # 물고기를 잡아서 먹음
            if 0 < graph[x][y] < shark_size:
                q = deque()
                visited = set((x, y))

                eat_fish += 1
                flag = True
                rst = time
                graph[x][y] = 0
                if eat_fish == shark_size:
                    shark_size += 1
                    eat_fish = 0

            # 못먹던 먹던 다음 위치의 값은 q에 저장 해야함,
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] <= shark_size and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))

            if flag:
                flag = False
                break

        time += 1

    print(rst)


n = int(input())
graph = []
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        if temp[j] == 9:
            shark_x, shark_y = i, j
            temp[j] = 0

    graph.append(temp)

find_fish(shark_x, shark_y)


"""
48. 16236 아기 상어 (Gold 4)
    - bfs 완전탐색 문제
    - 1) 처음 시도 했던 방법
      처음에 시도 했던 방법은 모든 물고기의 위치를 리스트-튜플로 저장해두고 
      graph를 초기화 시켜서 dist 맵으로 사용한 후, bfs를 사용해서 각각의 거리를 찾아 내서 이동시키는 방법이었다.
      구현력이 떨어져서 중간부터 코드가 꼬여서 포기했다. 

      위의 방법을 사용하면서 내가 전형적으로 구현력이 떨어지는 모습을 보였다. -> 계속되는 구현력의 문제점 발견!!
    
    - 2) 책에서 나온 방법 (1과 유사)
      책에서 찾아보니 1번 방법과 유사했으나, 쿨하게 bfs() 함수를 따로 두고 함수 내부에서 dist를 구해서 리턴하는 함수,
      위의 함수를 사용해서 다음에 먹을 물고기를 찾아나가는 함수 find()를 따로 두어서 main()에서 반복적으로 
      물고기를 찾아내는 방법이었다. 가장 직관적으로 문제에 접근할 수 있는 방법이어서 바로 이해되었고,
      시간 복잡도 차이도 크게 나지 않았다. 
      
      여기서 내 문제점이 또 하나 발생되는데 메모리를 조금만 더 사용하는거에 너무 목메면서 코드를 작성하는 것 같다. 
      1번 방법을 썼을때, graph를 다 초기화 시키지 않고 그냥 같은 크기의 배열을 선언하고 사용했으면 됐는데
      무리하게 진행하다가 코드가 꼬이는 일이 발생했다.
      2번 방법을 사용하면서 메모리 조금 더 먹더라도 시/공간 복잡도에서 크게 차이가 없고 더 직관적으로 코드를 짤 수 있음을 배웠다.

    - 3) bfs 하나로 해결한 방식
      이 방법은 시간 복잡도가 가장 낮게 측정된 방법으로, while q 내부에서 현재 q에 저장된 모든 지점을 탐색하는 방법이다.
      하나의 loop를 돌고 난 후에 다음에 갈 수 있는 점을 모두 q에 저장하므로 다음 1s동안 갈 수 있는 지점을 미리 저장하고
      다음 loop에서 q의 모든 점을 탐색하는 방법이었다. 물론 물고기를 먹고 난 후에는 q와 visited를 초기화 해준다. 

      visited를 set()으로 활용하면서 visited[i]를 활용 할 때와 같은 O(1)의 시간 복잡도를 갖고 한 loop에서 모든 점을 
      탐색한다는 점이 다른 문제와는 다른 점이었다. 이해되기까지 꽤 시간이 걸렸다. 

    - 개인적인 생각으로 좋은 문제인 것 같다. 
      solved.ac 기준 class03의 가장 높은 난이도의 문제이고, 기본적인 bfs의 문제가 아닌 
      bfs 응용력과 더불어 약간의 구현력을 포함하는 좋은 문제인 것 같다. 
"""
