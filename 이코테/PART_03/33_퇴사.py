import sys

input = sys.stdin.readline


def solution1():
    n = int(input())
    graph = []
    for _ in range(n):
        t, p = map(int, input().split())
        graph.append((t, p))

    dp = [0] * n

    for i in range(n):
        if i + graph[i][0] <= n:
            max_value = 0
            for j in range(i):
                if j + graph[j][0] <= i:
                    max_value = max(max_value, dp[j])

            dp[i] = max_value + graph[i][1]

    print(max(dp))


def solution2():
    n = int(input())
    graph = []
    dp = [0] * (n + 1)
    for _ in range(n):
        t, p = map(int, input().split())
        graph.append((t, p))

    for i in range(n - 1, -1, -1):
        # 할 수 있는 일
        if i + graph[i][0] <= n:
            dp[i] = max(dp[i + 1], graph[i][1] + dp[i + graph[i][0]])
        else:
            dp[i] = dp[i + 1]

    print(max(dp))


# solution1()
solution2()


"""
33. 퇴사 (p377)
    1. solution1
    - 앞에서부터 돌면서 dp 값을 갱신해 나갔다. 
    1) i번째 일을 할 수 있으면, 
    2) i번째 일을 한다고 했을때, 이전 날짜들에서 i번째 날짜 전까지 겹치지 않고 할 수 있는 일의 dp값 중에
       최댓값을 선택해서 더해 dp[i]를 갱신한다. 

    2. solution2 
    - 뒤에서부터 돌면서
    1) i번째 일을 할 수 있으면,
    2) i + 1번째 일의 dp값과 (i번째 일 + i번째 일의 기간 이후에 저장된 dp값)을 비교해서 갱신한다. 
    
    3) solution2의 풀이는 i번째 일을 (선택/선택하지 않음)을 선택하는 풀이법

    - 1번 풀이가 더 직관적으로 와닿으나, 효율적으로 푸는건 2번 풀이인것같다. 
"""