import sys

N = int(sys.stdin.readline())
As = list(map(int, sys.stdin.readline().split()))

max_val = max(As)

for idx, A in enumerate(As):
    As[idx] = A / max_val * 100

print(round(sum(As) / N, 3))
