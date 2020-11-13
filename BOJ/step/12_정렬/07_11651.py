import sys

n = int(sys.stdin.readline())

coord_lst = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coord_lst.append((x, y))


coord_lst.sort(key=lambda x: (x[1], x[0]))  # 람다식 익히기

for i in range(n):
    print(coord_lst[i][0], coord_lst[i][1])
