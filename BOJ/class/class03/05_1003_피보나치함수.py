# 피보나치 수열에서 함수 호출 횟수는 다시 피보나치 수열을 따른다. -> 당연함

t = int(input())
dp = [(1, 0), (0, 1)]

for _ in range(t):
    n = int(input())

    # 1. n < 2 이면 dp 값 출력
    if n < 2:
        print(dp[n][0], dp[n][1])
        continue

    # 2. 이전에 계산해서 dp에 저장한 값이면 출력
    if n < len(dp):
        print(dp[n][0], dp[n][1])
        continue
    else:  # 3. 이전에 계산하지 않은 값이면, 계산 후
        for i in range(len(dp), n + 1):
            zero = dp[i-1][0] + dp[i-2][0]
            one = dp[i-1][1] + dp[i-2][1]

            dp.append((zero, one))

        print(dp[n][0], dp[n][1])  # 출력한다.
