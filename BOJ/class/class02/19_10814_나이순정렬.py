import sys
input = sys.stdin.readline

n = int(input())
oj_members = []


for _ in range(n):
    age, name = input().split()
    oj_members.append((int(age), name))

oj_members = sorted(oj_members, key=lambda x: x[0])

for age, name in oj_members:
    print(age, name)
