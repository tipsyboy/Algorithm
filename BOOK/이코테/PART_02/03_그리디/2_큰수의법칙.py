import sys

n, m, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

first = numbers[-1]
second = numbers[-2]

q = m // (k + 1)
r = m % (k + 1)

print(q * (first * k + second) + r * first)
