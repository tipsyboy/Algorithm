
# 1
import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())


result = str(A * B * C)

for i in range(10):
    count = 0
    for j in range(len(result)):
        if i == int(result[j]):
            count += 1
    print(count)

######################################

# 2
# import sys

# A = int(sys.stdin.readline())
# B = int(sys.stdin.readline())
# C = int(sys.stdin.readline())

# result = list(str(A * B * C))

# for i in range(10):
#     print(result.count(str(i)))  # count() 함수

