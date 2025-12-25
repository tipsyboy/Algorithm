import sys

input = sys.stdin.readline

N = int(input())
ans = 0
for now in range(1, N + 1):
    # N까지 자연수에서 now를 약수로 갖는 수의 개수 (N // now)에 now를 곱해줘서 합을 구함
    ans += (N // now) * now  

print(ans)


"""
17425. 약수의 합 2
    - 1. 일반적으로 √n까지 확인해서 약수를 구하는 방법으로 실행했고 TLE - O(n√n)
    
    - 2. N의 배수는 항상 N을 약수로 갖는다.
      따라서, N까지 자연수에서 now를 약수로 갖는 수의 개수 (N // now)에 now를 곱해줘서 합을 구함
      O(N)
"""