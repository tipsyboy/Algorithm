import sys

input = sys.stdin.readline


def shortest_edit(string1, string2):
    n = len(string1)
    m = len(string2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    #
    for i in range(n + 1):
        dp[i][0] = i
    for i in range(m + 1):
        dp[0][i] = i

    #
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[n][m]


string1 = input().rstrip()
string2 = input().rstrip()

print(shortest_edit(string1, string2))


"""
15483. 최소 편집 (Gold 3)
    - dp 문제로 문자열을 비교해 나가는데 이미 비교한 문자까지는 다시 계산할 필요가 없다는 것에서 출발한다. 

    - 문자열 A -> B를 만드는데, A를 세로축, B를 가로축에 위치시켜서 dp[i][j]를 만들어 나간다. 
      왼쪽에서 오는 경우를(삽입), 왼쪽 위를(편집), 위에서 오는 경우를(삭제) 라고 하면
      이 2차원 dp가 어떻게 작동하게 되는지 알 수 있다. 

    - 따라서 현재 문자가 두 문자열에서 같은 경우는 같은 문자를 하나씩 추가한 경우이므로 왼쪽 대각선 위의 수를 그대로 가져오고
      그렇지 않은 경우는 삽입/편집/삭제 중에서 가장 작은 수를 선택해 현재 연산수인 +1을 추가해서 dp를 채워나가면 된다. 
"""