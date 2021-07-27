import sys
input = sys.stdin.readline


# 먼지 확산
def spread_dust():
    spread_map = [[0] * c for _ in range(r)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(r):
        for j in range(c):
            if graph[i][j] >= 5:  # 먼지의 양이 5 이상이 아니면 어차피 /5 하고 소수점 버렸을 때, 0임
                count = 0
                temp = graph[i][j] // 5

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        spread_map[nx][ny] += temp
                        count += 1

                graph[i][j] -= temp * count

    for i in range(r):
        for j in range(c):
            graph[i][j] += spread_map[i][j]


def move_air(up, low):
    # 위쪽 공기청정기
    for i in range(up-2, -1, -1):  # 왼
        graph[i+1][0] = graph[i][0]

    for i in range(1, c):  # 위
        graph[0][i-1] = graph[0][i]

    for i in range(1, up + 1):  # 오른
        graph[i-1][c-1] = graph[i][c-1]

    for i in range(c-2, 0, -1):  # 아래
        graph[up][i+1] = graph[up][i]
    graph[up][1] = 0

    # 아랫쪽 공기청정기
    for i in range(low+2, r):  # 왼
        graph[i-1][0] = graph[i][0]

    for i in range(1, c):  # 아래
        graph[r-1][i-1] = graph[r-1][i]

    for i in range(r-2, low-1, -1):  # 오른
        graph[i+1][c-1] = graph[i][c-1]

    for i in range(c-2, 0, -1):
        graph[low][i+1] = graph[low][i]
    graph[low][1] = 0


def check_dust():
    rst = 2

    for i in range(r):
        for j in range(c):
            rst += graph[i][j]

    return rst


r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치 찾기
for i in range(r):
    if graph[i][0] == -1:
        air_cleaner = i
        break


for _ in range(t):
    spread_dust()
    move_air(air_cleaner, air_cleaner + 1)


print(check_dust())

# ###############################################################################
# # 2) python으로 통과했다. spread_dust() 부분에서 for문으로 4방향을 검사하지 않고
# # 조건문으로 되는 것만 처리하는 방식으로 시간복잡도를 줄였다.
# # 통과해서 좋긴한데, 이게 좋은 방법인지는 모르겠다...
# input = sys.stdin.readline


# # 먼지 확산
# def spread_dust():
#     temp = [[0] * c for _ in range(r)]  # 확산값 저장

#     for i in range(r):
#         for j in range(c):
#             if graph[i][j] >= 5:
#                 val = 0  # 얼마나 확산했는지
#                 # 상
#                 if i - 1 >= 0 and graph[i - 1][j] != -1:
#                     temp[i - 1][j] += graph[i][j] // 5
#                     val += graph[i][j] // 5
#                 # 하
#                 if i + 1 < r and graph[i + 1][j] != -1:
#                     temp[i + 1][j] += graph[i][j] // 5
#                     val += graph[i][j] // 5
#                 # 좌
#                 if j - 1 >= 0 and graph[i][j - 1] != -1:
#                     temp[i][j - 1] += graph[i][j] // 5
#                     val += graph[i][j] // 5
#                 # 우
#                 if j + 1 < c and graph[i][j + 1] != -1:
#                     temp[i][j + 1] += graph[i][j] // 5
#                     val += graph[i][j] // 5
#                 temp[i][j] -= val  # 확산값 빼기

#     for i in range(r):
#         for j in range(c):
#             graph[i][j] += temp[i][j]  # 확산받은 값 더하기


# def move_air(up, low):
#     # 위쪽 공기청정기
#     for i in range(up-2, -1, -1):  # 왼
#         graph[i+1][0] = graph[i][0]

#     for i in range(1, c):  # 위
#         graph[0][i-1] = graph[0][i]

#     for i in range(1, up + 1):  # 오른
#         graph[i-1][c-1] = graph[i][c-1]

#     for i in range(c-2, 0, -1):  # 아래
#         graph[up][i+1] = graph[up][i]
#     graph[up][1] = 0

#     # 아랫쪽 공기청정기
#     for i in range(low+2, r):  # 왼
#         graph[i-1][0] = graph[i][0]

#     for i in range(1, c):  # 아래
#         graph[r-1][i-1] = graph[r-1][i]

#     for i in range(r-2, low-1, -1):  # 오른
#         graph[i+1][c-1] = graph[i][c-1]

#     for i in range(c-2, 0, -1):
#         graph[low][i+1] = graph[low][i]
#     graph[low][1] = 0


# def check_dust():
#     rst = 2

#     for i in range(r):
#         for j in range(c):
#             rst += graph[i][j]

#     return rst


# r, c, t = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(r)]

# # 공기청정기 위치 찾기
# for i in range(r):
#     if graph[i][0] == -1:
#         air_cleaner = i
#         break


# for _ in range(t):
#     spread_dust()
#     move_air(air_cleaner, air_cleaner + 1)


# print(check_dust())

"""
29. 17144 미세먼지 안녕! (Gold 5)
    - 구현에 시뮬레이션 문제
    
    - 약간의 생각을 포함한 빡구현 문제라고 생각했다. 
      move_air()에서 먼지가 이동하는데, 풀면서도 이게 맞나... 싶었지만, 제출하고 나니까 다들 이런식으로 풀었더라..

      python3로는 시간초과가 났고, pypy3로 제출해서 첫 번째에 AC했다.

    - 2번 코드에서 spread_dust() 부분에서 모든 먼지에 대해서 4방향 검사를 하지 않고,
      되는 부분만 처리하도록 풀어서 작성해서 최적화 시켜서 python3에서도 통과했지만, 
      이런식으로 최적화 하는 부분이 맞는가.. 싶기도 하는 생각이 들었다. 

    - 구현/시뮬레이션 문제에서 내가 맞다고 생각하면 끈기를 갖고 계속 풀어나가는 것이 중요하다는 것을 알았다. 
      코드를 작성하는 것은 어느정도는 노가다가 당연히 필요하니까..?
"""
