# 현재 나이트의 위치
coord_val = input()
x, y = int(coord_val[1]), (ord(coord_val[0]) - ord("a") + 1)

# 나이트가 갈 수 있는 방향
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
count = 0  # 나아갈 수 있는 방향의 가짓 수

for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

print(count)
