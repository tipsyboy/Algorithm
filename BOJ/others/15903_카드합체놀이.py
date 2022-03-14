import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline


def solution(n, m, cards):
    heapify(cards)

    for _ in range(m):
        a = heappop(cards)
        b = heappop(cards)

        heappush(cards, a + b)
        heappush(cards, a + b)

    return sum(cards)


n, m = map(int, input().split())
cards = list(map(int, input().split()))

print(solution(n, m, cards))
