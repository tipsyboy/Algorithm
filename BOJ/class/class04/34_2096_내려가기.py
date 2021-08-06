import sys

input = sys.stdin.readline

n = int(input())
max_dp = [[0] * 3 for _ in range(2)]
min_dp = [[0] * 3 for _ in range(2)]

for _ in range(n):
    temp = list(map(int, input().split()))

    max_dp[1][0] = max(max_dp[0][0], max_dp[0][1]) + temp[0]
    min_dp[1][0] = min(min_dp[0][0], min_dp[0][1]) + temp[0]

    max_dp[1][1] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + temp[1]
    min_dp[1][1] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + temp[1]

    max_dp[1][2] = max(max_dp[0][1], max_dp[0][2]) + temp[2]
    min_dp[1][2] = min(min_dp[0][1], min_dp[0][2]) + temp[2]

    max_dp[0][0], max_dp[0][1], max_dp[0][2] = max_dp[1][0], max_dp[1][1], max_dp[1][2]
    min_dp[0][0], min_dp[0][1], min_dp[0][2] = min_dp[1][0], min_dp[1][1], min_dp[1][2]


print(max(max_dp[0]), min(min_dp[0]))


"""
34. 2096 내려가기 (Gold 4)
    1. 첫 번째 생각
    - graph를 받고 dp테이블을 따로 생성해서 전형적인 dp라고 생각하고 문제를 풀었다. 
    
    - MLE 받음
    
    2. 두 번째 생각
    - 솔직히 평소에 문제를 풀면서 MLE는 거의 생각하지 않고 풀기 때문에 어떻게 해야할지 감이 잘 안잡혔다. 
    
    - dp테이블을 graph대로 생성하지 않고 2개행만 생성해서 풀었다. 역시 MLE 받았다.

    3. 세 번째 생각
    - 구글링을 통해서 찾아보니까 아예 graph를 저장하는 것 자체를 하지 않았다. 
      그냥 매 행마다 리스트로 입력값을 받아서 2*3 리스트를 통해서 값을 계산했다.  
    
    - AC

    - 전형적인 dp문제로 dp라고 하기에는 난이도 책정이 높게 되었기 때문에 좀 의문이 있었으나 태그에 슬라이딩 윈도우 태그가 함께 있었다.
      슬라이딩 윈도우라고 하면 그냥 비교되는 값들을 저장하지 않고 최소화 하는 정도로만 생각하고 있었는데, 
      아예 문제의 입력 값을 저장하는 것조차 최소화 해서 사용할 수 있다는 것을 알게됨.

    - 메모리가 크게 제한된 문제들은 아직 감을 잡지 못하는 것 같다.
      또 슬라이딩 윈도우 문제에 대해서도 아직 잘 와닿지가 않긴함.
"""