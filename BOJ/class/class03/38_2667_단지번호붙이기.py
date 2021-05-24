import sys
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global building  # 집의 개수

    # graph 범위 초과
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 현재 위치 (x, y)가 집이 있는 곳 이면,
    if graph[x][y] == 1:
        graph[x][y] = 0  # 방문 처리
        building += 1  # 집 개수 하나 증가
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

        return True

    return False  # 집이 없는 곳이면, return False


n = int(input())
# map() 사용을 위해서는 iterable한 객체를 대상으로 하므로 string으로 캐스팅해서 입력을 받는다.
graph = [list(map(int, str(input().rstrip()))) for _ in range(n)]
building = 0  # 집의 개수
unit = 0  # 단지의 개수
units = []  # 단지에 포함된 집의 개수

for i in range(n):
    for j in range(n):
        if dfs(i, j):  # dfs() 수행 결과 단지가 있으면 (return 값이 True)
            unit += 1  # 단지 수 증가
            units.append(building)  # 이번 단지의 집의 개수 저장
            building = 0  # 집의 수 초기화

print(unit)
units.sort()
for i in units:
    print(i)


# ### 2) bfs로 구현하기
# import sys
# from collections import deque
# input = sys.stdin.readline


# def bfs(start_x, start_y):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     q = deque([(start_x, start_y)])  # 시작점 q에 추가
#     building = 1  # 집의 수 (현재 시작점 q에 추가하므로 1부터 시작)
#     graph[start_x][start_y] = 0  # 현재 점 방문 처리

#     # bfs
#     while q:
#         x, y = q.popleft()  # (now_x, now_y)

#         for i in range(4):
#             # next x, y
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # 이동 가능한 위치 and 해당 위치에 집이 있으면,
#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] == 1:
#                     graph[nx][ny] = 0  # 방문 처리
#                     q.append((nx, ny))  # que에 추가
#                     building += 1  # 집의 개수 증가

#     return building  # 집의 수 리턴


# n = int(input())
# graph = [list(map(int, str(input().rstrip()))) for _ in range(n)]
# units = []  # 단지마다 집의 수
# unit = 0  # 단지 수

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:  # 집이 있는 위치에서 bfs시작
#             units.append(bfs(i, j))
#             unit += 1  # 단지 수 증가

# units.sort()
# print(unit)
# for i in units:
#     print(i)
# print(unit, units)


"""
- graph 입력부분이 공백으로 구분되는 경우가 아닌 케이스가 class3 에서 연속으로 나오는데,
  map() 함수를 공부하는데 좋았던듯 (iterable 객체)

1) dfs로 구현
    - 처음 보자마자 책에서 아이스크림 얼려먹기 문제가 생각나서 풀었다.
      dfs 구현은 bfs에 비해서 살짝 익숙하지 않은 감이 있고, 
      재귀함수 리턴부분은 역시 아직도 헷갈리는 부분인 것 같다. 

2) bfs로 구현
    - bfs 구현은 dfs보다는 익숙한 완전탐색 기법이지만, 시작 점의 집의 수를 세지 않는 문제가 생겨서
      처음에 틀렸다. 이후에 building = 1로 스타트 했지만, bfs 방문처리상 처음 방문 좌표가 1로
      되어 있어서 두번째 점에서 시작점을 q에 추가하는 문제가 생겼다. 
      따라서 bfs() 호출시 q에 시작점을 추가하는 시점에서 (집의 수, 시작점 방문처리, q에 추가)를 수행해서
      해결했다.
"""
