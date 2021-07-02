import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 물건 개수, 최대 무게
things = []  # 물건 무게 / 가치
dp = [[0] * (k+1) for _ in range(n+1)]
for _ in range(n):
    w, v = map(int, input().split())  # 물건 무게 / 가치
    things.append((w, v))  # 튜플로 저장


for i in range(1, n+1):  # 현재 물품
    w, v = things[i-1]  # 현재 물품 무게 / 가치
    for j in range(1, k+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])

# print(dp)
print(dp[-1][-1])


"""
11. 12865 평범한 배낭 (Gold 5)
    - 유명한 dp문제로 0-1 knapsack 문제라고도 한다. 

    - 첫 번째 생각으로는 받은 무게/가치 리스트를 소팅한 후에 
      가지고 갈 수 있는 물건의 개수를 행에 가지고 갈 수 있는 용량을 열에 놓고 확인하려고 했으나,
      그렇게 되면 나올 수 있는 경우의 수를 모두 조합해야 한다는 것을 알게됨.

    - 조금 찾아본 결과 i번째 물건에 집중해서 i번째 물건을 넣을수 있는가/없는가에 집중해서 테이블을 
      채워나가면 된다는 힌트를 얻었다.
      현재 물건 i가 현재 용량 w에 들어갈 수 없으면 이전 최대 값을 사용하고, 
      들어갈 수 있으면, w-현재 물건 i의 차만큼 다시 테이블에서 찾아서 value를 비교해줘서 큰 값을 가져간다. 
    
    - dp를 공부하는데 많은 도움이 되는 문제였다. 
"""
