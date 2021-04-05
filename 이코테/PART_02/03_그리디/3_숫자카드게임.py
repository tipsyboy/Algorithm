import sys

n, m = map(int, sys.stdin.readline().split())
rst = 0
# cards = []

# for i in range(n):
#     temp = list(map(int, sys.stdin.readline().split()))
#     cards.append(temp)

for i in range(n):
    temp_lst = list(map(int, sys.stdin.readline().split()))
    temp = min(temp_lst)

    rst = max(rst, temp)


print(rst)
