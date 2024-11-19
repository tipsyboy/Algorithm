# 2024.11.10 SUN
# https://www.acmicpc.net/problem/23977

import sys
from math import lcm

input = sys.stdin.readline

K, N = map(int, input().split())
A = list(map(int, input().split()))

# 비밀번호를 배열 A의 원소들로 각각 나누었을 때, 나누는 수와 그 나머지의 차이는 K로 동일하다.
# 비밀번호는 두 번째 규칙을 만족하는 수 중 가장 작은 양의 정수이다.

print(lcm(*A) - K)
