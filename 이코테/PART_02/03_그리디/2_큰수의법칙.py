import sys

n, m, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
q = m // k
r = m % k
rst = q * (num[-1] * k) + (num[-2] * r)

print(rst)
