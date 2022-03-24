# 남쪽 이동
def s_rotate(dice):
    temp = dice[1:4] + [dice[0]]
    dice = temp + dice[4:]

    return dice


# 북쪽 이동
def n_rotate(dice):
    temp = [dice[3]] + dice[:3]
    dice = temp + dice[4:]

    return dice


# 동쪽 이동
def e_rotate(dice):
    temp = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[2]
    dice[2] = dice[5]
    dice[5] = temp

    return dice


# 서쪽 이동
def w_rotate(dice):
    temp = dice[0]
    dice[0] = dice[5]
    dice[5] = dice[2]
    dice[2] = dice[4]
    dice[4] = temp

    return dice


n, m, y, x, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
command = list(map(int, input().split()))

dy = [0, 0, -1, 1]  # 동 서 북 남
dx = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]  # 밑, 정, 윗, 뒷, 동, 서 면
for com in command:
    ny = y + dy[com - 1]
    nx = x + dx[com - 1]

    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        continue

    if com == 1:
        dice = e_rotate(dice)
    elif com == 2:
        dice = w_rotate(dice)
    elif com == 3:
        dice = n_rotate(dice)
    elif com == 4:
        dice = s_rotate(dice)

    if graph[ny][nx]:
        dice[0] = graph[ny][nx]
        graph[ny][nx] = 0
    else:
        graph[ny][nx] = dice[0]
    y = ny
    x = nx

    print(dice[2])
