import sys

input = sys.stdin.readline

N, M = map(int, input().split())

name_to_num = dict()
num_to_name = dict()
for i in range(1, N + 1):
    name = input().rstrip()
    name_to_num[name] = i
    num_to_name[i] = name

for _ in range(M):
    query = input().rstrip()

    if query.isnumeric():
        print(num_to_name[int(query)])
    else:
        print(name_to_num[query])


"""
1620. 나는야 포켓몬 마스터 이다솜

    - 기본 해시맵 문제
      파이썬의 dict()를 통해서 해결
"""