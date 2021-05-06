t = int(input())

dp = [1, 2, 4]

for i in range(7):
    dp.append(dp[i] + dp[i+1] + dp[i+2])

for _ in range(t):
    n = int(input())
    print(dp[n-1])

"""
ex) 4인 경우 - dp3인 경우에 +1 / dp2인 경우에 +2 / dp1인 경우에 +3

인 경우의 수를 생각해 볼 수 있다. 
따라서 n항의 n-1, n-2, n-3항의 dp 경우의 수를 합한 값이 n번째 값이 됨

"""
