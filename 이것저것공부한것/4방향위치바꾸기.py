x, y = 2, 1  # 현재 위치가 (2, 1)

# 동 남 서 북 순서로 0, 1, 2, 3
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  # 현재 바라보고 있는 위치


for i in range(1, 11):

    # change of right direction 90 degree
    if i % 3 == 0:
        direction = (direction + 1) % 4

    x = x + dx[direction]
    y = y + dy[direction]

    print(f"{i}초 후 현재 위치: {x, y}")
