import sys
import random
import time

input = sys.stdin.readline

# 1)
def solution(n, data):
    data_dict = dict()
    rst = 0

    for d in data:
        data_dict[d] = data_dict.get(d, 0) + 1

    for value in data_dict.values():
        n -= value
        rst += n * value  # 마지막 원소는 사실 안해도 되지만 어차피 n = 0 이되면서, 0을 더하는 값이 된다.

    return rst


# 2) 해설지 풀이
def solution2(n, data):
    weight = [0] * 11
    rst = 0

    for b in data:
        weight[b] += 1

    for i in range(1, m + 1):
        n -= weight[i]
        rst += weight[i] * n

    return rst


# 3) 막 풀이
def solution3(n, data):
    rst = 0

    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] != data[j]:
                rst += 1

    return rst


n, m = map(int, input().split())
# data = list(map(int, input().split()))
data = []

for i in range(n):
    data.append(random.randint(1, m))

print(solution(n, data))
print(solution2(n, data))
print(solution3(n, data))

"""
05. 볼링공 고르기
    - 이 문제는 최대 선택 개수가 10C2를 수행하고, n의 범위가 1 <= n <= 1000 이므로 
      3번 풀이처럼 풀어도 1s가 넘지 않을 것이지만, 조합을 생각해서 푸는게 가장 좋은 풀이이다.

    - sol2는 해설지 풀이이다. 
"""
