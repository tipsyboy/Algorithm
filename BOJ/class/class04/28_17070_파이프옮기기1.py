import sys
input = sys.stdin.readline


def move_pipe(x, y, d):
    # 현재 방향에서 갈 수 있는 이동의 방식들 - 0: 가로, 1: 세로, 2: 대각선
    directions = {0: (0, 2), 1: (1, 2), 2: (0, 1, 2)}
    next_positions = {0: (0, 1), 1: (1, 0), 2: (1, 1)}

    for direction in directions[d]:
        nx = x + next_positions[direction][0]
        ny = y + next_positions[direction][1]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1:
            # 대각선인 경우
            if direction == 2:
                if graph[nx-1][ny] == 0 and graph[nx][ny-1] == 0:
                    dp[nx][ny][direction] += dp[x][y][d]
            else:
                dp[nx][ny][direction] += dp[x][y][d]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(3):
            if dp[i][j][k] != 0 and graph[i][j] == 0:
                move_pipe(i, j, k)

print(sum(dp[n-1][n-1]))


"""
28. 17070 파이프 옮기기1 (Gold 5)
    - 너무 어려웠다..
      dp라는 것은 대충 눈치 채고 dp로 접근 하려고 했으나, 내가 생각하는 방향이랑 너무 달랐던 것 같다. 

    - 문제는 3차원 dp를 사용하는 방식으로 해결했으나, 3차원 dp를 한번도 해본 적이 없어서
      이해하는데 오랜 시간이 걸렸음.
      3차원 배열부터는 너무 구체적으로 그려보려고 하지말고 추상적인 그 상태 자체로 이해 하는 것이 편한것 같다. 
      
    - 문제에서는 이동만 할 수 있으면 이전 파이프를 이동하는 것이므로 +1 등등의 횟수를 저장하는 것이 아니라
      이전 파이프에서 이동만 할 수 있으면 그대로 값을 가져온다.
      다만 이전에 같은 위치로 다른 방식으로 들어와 있을 수 있는 경우가 있기 때문에
      +=를 통해서 이번 경로로 들어온 것을 추가해 준다. 
    
    - dp는 (x, y) 방향에서 뻗은 방향 d를 갖고 있는 방식이다.
      why? -> 현재 문제에서 파이프는 앞으로만 이동이 가능하고, 뒤에 있는 점이 next position으로 이동할 수 있으면, 
      앞에 있는 점은 뒷점을 그대로 밟기 때문이다.(graph를 넘거나 하지 않고) 
      이때, 대각선은 추가로 두 위치에 대한 체크를 해줘야 하기 때문에 조건문으로 추가적인 판단 이후에 dp에 추가한다. 
      

      
"""


# # n == 3
# [
# 	[
# 	    [0, 0, 0], [1, 0, 0], [1, 0, 0]
# 	],
# 	[
# 	    [0, 0, 0], [0, 0, 0], [0, 0, 1]
# 	],
# 	[
# 	    [0, 0, 0], [0, 0, 0], [0, 1, 0]
# 	]
# ]


# # n == 4
# [
#     [
# 	    [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]
#     ],
#     [
# 	    [0, 0, 0], [0, 0, 0], [0, 0, 1], [1, 0, 1]
#     ],
#     [
# 	    [0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 1]
#     ],
#     [
# 	    [0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 2, 1]
#     ]
# ]
