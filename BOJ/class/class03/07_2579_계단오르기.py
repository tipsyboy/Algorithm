n = int(input())
scores = [0]

for _ in range(n):
    scores.append(int(input()))

if n == 1:
    print(scores[1])
elif n == 2:
    print(scores[1] + scores[2])
else:
    dp = [0] * (n + 1)

    dp[1] = scores[1]
    dp[2] = scores[1] + scores[2]

    for i in range(3, n+1):
        # 1. n-1을 밟는 경우, n-2를 밟는 경우 중 큰 경우
        dp[i] = max(scores[i-1] + dp[i-3], dp[i-2]) + scores[i]

    print(dp[n])
