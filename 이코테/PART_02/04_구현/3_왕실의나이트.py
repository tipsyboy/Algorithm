import sys

input = sys.stdin.readline

knight = input().rstrip()
x = int(knight[1]) - 1
y = ord(knight[0]) - ord("a")

steps = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2), (2, -1), (2, 1)]
rst = 0

for i in range(8):
    nx = x + steps[i][0]
    ny = y + steps[i][1]

    if 0 <= nx < 8 and 0 <= ny < 8:
        rst += 1

print(rst)