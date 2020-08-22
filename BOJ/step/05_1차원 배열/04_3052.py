# 1
import sys
As = [int(sys.stdin.readline()) % 42 for i in range(10)]
As = set(As)
print(len(As))


# 2
# As = set()

# for i in range(10):
#     n = int(input())
#     As.add(n % 42)

# print(len(As))
