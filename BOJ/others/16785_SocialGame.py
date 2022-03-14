
# a, b, c = map(int, input().split())

# x = 0
# while True:
#     if a * x + (x // 7) * b >= c:
#         break

#     x += 1

# print(x)


## 2.
from math import ceil

a, b, c = map(int, input().split())

week = a * 7 + b

m, r = divmod(c, week)

print(m * 7 + min(ceil(r / a), 7))
