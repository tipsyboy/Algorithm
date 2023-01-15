import sys

input = sys.stdin.readline

N = int(input())
*arr, target = map(int, input().split())
dp = [[0] * 21 for _ in range(N - 1)]

dp[0][arr[0]] = 1  # 첫 번째 수
for i in range(1, N - 1):
    now = arr[i]  # 이번 숫자

    for j in range(21):
        # 1. 이전 숫자에서 만든 값이 아니면 넘어감 -> i-1번째 수로 만들었던 수식이 유효했어야함
        if dp[i - 1][j] == 0:
            continue

        # 2. i-1번째에서 유효했던 숫자에서 i번째 숫자를 빼거나 더했을때 유효해야 한다.
        if 0 <= j - now < 21:
            dp[i][j - now] += dp[i - 1][j]
        if 0 <= j + now < 21:
            dp[i][j + now] += dp[i - 1][j]

# print(*dp, sep="\n")
print(dp[N - 2][target])


"""
5557. 1학년
    - dp

    - 0~20의 범위의 수를 계속 만들어나감 
      재귀로 모든 경우의 수를 탐색하는 경우 TLE

    - i번째 숫자로 만들 수 있는 수를 0~20의 범위에서 만들려면 
      1. i-1번째 숫자가 유효 했어야 한다. 
      2. i-1번째에서 유효했던 숫자에서 i번째 숫자를 빼거나 더했을때 유효해야 한다.
      3. 2.에서 찾아간 idx의 경우의 수가 이번 경우의 수에 추가된다. 
"""