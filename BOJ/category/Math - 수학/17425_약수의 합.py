import sys

input = sys.stdin.readline
MAXV = 10 ** 6

divisor_sum = [1] * (MAXV + 1)
for i in range(2, MAXV + 1):
    for j in range(i, MAXV + 1, i):
        divisor_sum[j] += i

psum = [0]
for i in range(1, MAXV + 1):
    psum.append(divisor_sum[i] + psum[-1])


TC = int(input())
for _ in range(TC):
    N = int(input())
    print(psum[N])

"""
17425. 약수의 합
    - 자연수 i의 배수는 항상 i를 약수로 갖는다. 

    - 위의 개념을 갖고 에라토스테네스의 체 처럼 해결
    
    - 매 테스트 케이스마다 sum 연산을 하면 TLE가 나오므로 prefix sum을 통해서 해결
"""