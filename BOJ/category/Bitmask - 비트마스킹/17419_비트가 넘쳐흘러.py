# 2024.07.31 WED
# https://www.acmicpc.net/problem/17419

"""
17419. 비트가 넘쳐흘러
K = K-(K&((~K)+1))
  ~K + 1 -> 비트 반전 후 +1 -> 2의 보수 -> -K
  K&(-K) -> K의 마지막 비트 
  K - (K&(-K)) -> K의 마지막 비트를 지움

따라서, 0이 될 때까지 마지막 비트를 하나씩 지움
"""


import sys

input = sys.stdin.readline

N = int(input())
K = input().rstrip()
print(K.count("1"))
