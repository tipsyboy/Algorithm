import sys
input = sys.stdin.readline

n = int(input())
numbers = []

# 입력
for _ in range(n):
    numbers.append(int(input()))

numbers = sorted(numbers)  # 정렬

# print("\n".join(map(str, numbers)))  # 출력

for number in numbers:
    print(number)
