import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # arr length, test case
arr = list(map(int, input().split()))

prefix_sum = [0 for _ in range(n + 1)]

# init prefix sum list
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

# test case
for _ in range(m):
    start, end = map(int, input().split())

    print(prefix_sum[end] - prefix_sum[start-1])
