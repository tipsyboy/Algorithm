import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):  # 현재 기준점 (현재 들어온 수열에 들어온 값이라고 생각해도 됨)
    for j in range(i):  # 앞서 있었던 길이들 비교
        if seq[i] < seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))