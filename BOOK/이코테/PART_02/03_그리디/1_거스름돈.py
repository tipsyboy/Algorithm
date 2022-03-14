import sys

n = int(sys.stdin.readline())  # change
coin_types = [500, 100, 50, 10]
cnt = 0

for coin in coin_types:
    cnt += n // coin
    n = n % coin

    if n == 0:
        break


print(cnt)
