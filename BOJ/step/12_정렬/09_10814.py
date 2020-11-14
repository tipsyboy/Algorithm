import sys

n = int(sys.stdin.readline())

members = []

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    members.append((int(age), name))

members.sort(key=lambda x: x[0])  # 나이 기준 정렬

for i in range(n):
    print(members[i][0], members[i][1])
