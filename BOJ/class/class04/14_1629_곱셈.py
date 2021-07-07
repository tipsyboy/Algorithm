import sys
input = sys.stdin.readline


# # a**b%c를 리턴하는 함수
# def solve(a, b):
#     if b == 1:
#         return a % c

#     # b(나누는 수)가 짝수
#     if b % 2 == 0:
#         return (solve(a, b//2) ** 2) % c
#     else:  # 홀수
#         return (solve(a, (b-1)//2) ** 2) * a % c


a, b, c = map(int, input().split())
# print(solve(a, b))

# # 2) pow()함수가 해결해 주더라
# print(pow(a, b, c))

"""
14. 1629 곱셈 (Silver 1)
    - 후.. 코드가 간단해 보이지만 꽤 오래 걸렸던 문제.

    - 수가 너무 크므로 각 연산에서 %C를 필수로 해주어야 하고, 
      제곱하는 수 B값을 계속해서 줄여나간다. 

    - 분할정복이 많이 약한것 같다...

    - 이진탐색 푸는거 같았다 ㅋㅋ... 
"""
