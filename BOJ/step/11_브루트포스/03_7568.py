
import sys

N = int(sys.stdin.readline())  # 총 인원
people = []  # 사람

# 몸무게, 키 저장
for i in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    people.append((weight, height))

for person in people:
    rank = 1  # 순위

    for target in people:
        if person == target:
            continue
        if person[0] < target[0] and person[1] < target[1]:
            rank += 1

    print(rank, end=" ")
