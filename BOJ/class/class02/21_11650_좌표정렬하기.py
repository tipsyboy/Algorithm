import sys
input = sys.stdin.readline

n = int(input())
coordinate = []  # 좌표

for _ in range(n):
    x_coord, y_coord = map(int, input().split())
    coordinate.append((x_coord, y_coord))

coordinate = sorted(coordinate, key=lambda x: (x[0], x[1]))

for x_coord, y_coord in coordinate:
    print(x_coord, y_coord)
