import sys

input = sys.stdin.readline
DIV = 1_000_000


def solution(N: list) -> int:
    if N[0] == 0:
        return 0

    dp = [0] * (len(N) + 1)
    dp[0] = dp[1] = 1
    for i in range(2, len(N) + 1):
        if N[i - 1] != 0:  # 1.
            dp[i] += dp[i - 1]
            dp[i] %= DIV
        if 9 < N[i - 2] * 10 + N[i - 1] < 27:  # 2.
            dp[i] += dp[i - 2]
            dp[i] %= DIV
    return dp[len(N)] % DIV


N = list(map(int, input().rstrip()))
print(solution(N))


"""
2011. 암호코드
    - dp 사용해서 해결

    - dp[i] =  
      1. 이번 차례 수가 0이 아니라면 i-1번째 까지에 이번 차례 수만 추가해주는 경우
      2. 바로 앞의 수와 합쳐서 새 알파벳을 만들 수 있는 경우의 수에는 i-2번째의 경우가 추가
      
      3. 암호가 유효하지 않는 경우를 찾으면, dp[i]를 갱신할 때, 
         조건이 맞지 않으면 더해주지 않기 때문에 자연스럽게 0을 출력할 수 있으니
         맨 처음 수가 0인 경우의 수만 제외한다. 
      4. 수가 커질 수 있으니 1_000_000으로 나눈 나머지를 사용한다. 
"""