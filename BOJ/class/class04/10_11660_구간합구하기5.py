import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 행 더하기
for i in range(n):
    for j in range(n-1):
        graph[i][j + 1] += graph[i][j]

# 열 더하기
for j in range(n):
    for i in range(n-1):
        graph[i + 1][j] += graph[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(graph[x2-1][y2-1])
    elif x1 == 1:
        print(graph[x2-1][y2-1] - graph[x2-1][y1-2])
    elif y1 == 1:
        print(graph[x2-1][y2-1] - graph[x1-2][y2-1])
    else:
        print(graph[x2-1][y2-1] - graph[x2-1][y1-2] -
              graph[x1-2][y2-1] + graph[x1-2][y1-2])


# # 2) 행렬을 하나씩 더 추가해서 합 배열을 따로 반드는 방법
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# s = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(n):
#     for j in range(n):
#         s[i + 1][j + 1] = (s[i + 1][j] + s[i][j + 1] - s[i][j]) + graph[i][j]

# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())

#     print(s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1])


"""
10. 11660 구간 합 구하기 5 (Silver 1)
    - 시작 좌표(x1, y1)에서 끝 좌표(x2, y2) 직사각형의 합을 구하는 문제로 전체 값을 먼저 구한후 
      정답에 쓸모 없는 구간을 빼는 방법으로 구간 합을 찾아냈다. 
      (0, 0)부터 시작 좌표까지의 값은 두 번 빼게 되므로 한번 다시 더해준다. 
    
    - map graph를 그대로 사용하면 좌표 값 -2를 해야되는데 이때, 예외처리가 발생한다. 
      메모리를 아낄수 있지만 조금 귀찮다.

    - map graph 테두리를 한칸씩 넓힌 합테이블을 하나 더 만들게 되면, 코드상으로 더 간단하게 구할 수 있지만,
      그만큼 메모리를 더 사용한다. 
"""
