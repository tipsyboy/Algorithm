import sys

input = sys.stdin.readline

remained_num = input().rstrip()

i = 0  # input받은 수의 index
num = 0  # N 판단할 수
while i < len(remained_num):
    num += 1
    num_str = str(num)
    if remained_num[i] in num_str:
        num_idx = num_str.index(remained_num[i])

        while i < len(remained_num) and num_idx < len(num_str):
            if num_str[num_idx] == remained_num[i]:
                i += 1
            num_idx += 1

print(num)


"""
1515. 수 이어쓰기 
    - 일부가 지워진 1..N의 수를 연속으로 쓴 문자열에서 N의 최솟값을 찾는 문제

    - 단순히 포함관계를 생각해서 풀면 1111111과 같은 반례로 틀린다. 
      남아 있는 수의 현재 숫자가 탐색하고 있는 숫자에 포함된다면 
      그때 탐색하고 있는 숫자와 남아있는 수의 일치하는 만큼을 전진시켜줘야 최적해를 찾을 수 있다. 
"""