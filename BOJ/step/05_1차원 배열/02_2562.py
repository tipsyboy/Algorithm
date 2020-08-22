import sys

# 1

As = [sys.stdin.readline() for i in range(9)]
As = list(map(int, As))
max_idx = 0

for i in range(1, 9):
    if As[max_idx] < As[i]:
        max_idx = i

print(As[max_idx])
print(max_idx+1)

# 2번
# As = [sys.stdin.readline() for i in range(9)]
# As = list(map(int, As))

# print(max(As))
# print(As.index(max(As)) + 1)
