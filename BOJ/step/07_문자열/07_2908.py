import sys

A, B = sys.stdin.readline().split()

A = int(A[::-1])  # [::-1] - 역순
B = int(B[::-1])

print(max(A, B))
