import sys

input = sys.stdin.readline

n, l = map(int, input().split())
x = -1
length = 0

for i in range(l, 101):
    sn = (i * (i - 1)) / 2

    if (n - sn) % i == 0 and (n - sn) // i >= 0:
        x = int((n - sn) // i)
        length = i
        break

if x == -1:
    print(-1)
else:
    for i in range(x, x + length):
        print(i, end=" ")
