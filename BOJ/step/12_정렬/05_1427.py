import sys

numbers = list(map(int, sys.stdin.readline().strip()))

numbers.sort(reverse=True)

for number in numbers:
    print(number, end="")
