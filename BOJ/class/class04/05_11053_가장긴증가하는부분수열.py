import sys
input = sys.stdin.readline


n = int(input())
seq = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            # 현재 기준 원소 i이 i이전의 값 j들을 루프를 돌면서 i보다 작은 값을 추가 한 리스트의 길이
            # 즉 dp[j] + 1과 현재까지 i의 LIS값(dp[i])를 비교한다.
            dp[i] = max(dp[i], dp[j] + 1)


print(dp)
print(max(dp))


# 반) 8
#     1 2 4 3 3 4 2 1

"""
05. 11053 가장 긴 증가하는 부분 수열 (Silver 2)
    - Longest Increasing Subsequence(LIS)
    
    - 리스트 전체를 순회하면서 자신(i)를 기준으로 자신을 포함하는 가장 긴 수열을 찾는다.
      즉, i이전의 값들을 탐색하면서 보면되며, 기준점이 점점 뒤로 가기 때문에 이전의 계산 값을
      참조해서 사용할 수 있다. -> 따라서 dp문제에 해당한다. 

    - 약간 이해하기 힘들었으나 이해하고 난 후에 보니, 전형적인 dp문제임을 알 수 있었다.
      (이전의 계산 값이 현재 계산하고자 하는 값에 관여함)

    - 메인 아이디어는 위와 같이 기준점 뒷쪽의 수열을 생각하지 않고 기준점 i를 포함하는 가장 긴 수열을
      차례로 만들어 나가는 것이다. (즉, 매번 기준점 i가 수열의 가장 큰 수가 된다.)
    
    - LIS에 대해서는 구글링 해보니 흥미로운 블로그 글을 하나 확인해서 훑어봤는데, 조금 헷갈려서
      나중에 보기로 하였다. 
"""
