import sys
from collections import Counter
input = sys.stdin.readline

# 1) collections module의 Counter class 사용
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = map(int, input().split())

cards = dict(Counter(cards))

for num in numbers:
    if num in cards:
        print(cards[num], end=" ")
    else:
        print(0, end=" ")
