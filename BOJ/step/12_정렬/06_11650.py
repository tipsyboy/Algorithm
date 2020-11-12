import sys

n = int(sys.stdin.readline())  # 수의 개수

coord_lst = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coord_lst.append((x, y))

coord_lst.sort()  # 그냥 y 좌표도 비교해서 sorting 해줌 ㅡㅡ

for i in range(n):
    print(coord_lst[i][0], coord_lst[i][1])


######

# for i in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     coord_lst.append((x, y))

# coord_lst.sort(key=lambda x: (x[0], x[1]))

# for i, j in coord_lst:
#     print(i, j)
