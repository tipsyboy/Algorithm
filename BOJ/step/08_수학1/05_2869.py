
import sys

A, B, V = map(int, sys.stdin.readline().split())

days = (V-B) / (A-B)

if days == int(days):
    print(int(days))
else:
    print(int(days) + 1)


# 1. 시간 초과함
# import sys

# A, B, V = map(int, sys.stdin.readline().split())
# days = 0  # 올라가는데 걸리는 일 수

# while True:
#     days += 1
#     if (A-B)*days >= V - B:
#         break

# print(days)
