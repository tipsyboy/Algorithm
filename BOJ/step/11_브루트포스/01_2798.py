

# 1) 삼중 for문을 이용한 하나씩 차례대로 비교
#  - 블랙잭의 경우에 빠져나오게 설정했는데, 더 느리다.. 왜 그럴까? - 그래서 지움.
import sys


n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result_max = 0
result_sum = 0
flag = False  # 블랙잭

for i in range(len(numbers)-2):
    for j in range(i+1, len(numbers)-1):
        for k in range(j+1, len(numbers)):
            if result_max <= numbers[i] + numbers[j] + numbers[k] <= m:
                result_max = numbers[i] + numbers[j] + numbers[k]

print(result_max)

####################################################################################

# # 2) 조합 사용 - 더 느림.. 왜일까
# import sys
# from itertools import combinations  # 조합

# n, m = map(int, sys.stdin.readline().split())
# numbers = list(map(int, sys.stdin.readline().split()))
# _sum = 0

# # 조합
# for combi in list(combinations(numbers, 3)):
#     if _sum < sum(combi) <= m:
#         _sum = sum(combi)
#     if _sum == m:  # 블랙잭
#         break

# print(_sum)
