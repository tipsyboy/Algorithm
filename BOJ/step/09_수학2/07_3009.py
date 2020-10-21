import sys

x_list = []
y_list = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())

    x_list.append(x)
    y_list.append(y)


# 직사각형이므로 좌표값이 한 개인 것이 나머지 한 점의 좌표가 된다.
for x_coord in x_list:
    if x_list.count(x_coord) == 1:
        x = x_coord
        break

for y_coord in y_list:
    if y_list.count(y_coord) == 1:
        y = y_coord
        break

print(x, y)
