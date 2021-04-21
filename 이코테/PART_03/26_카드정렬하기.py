import sys
import heapq

input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    heapq.heappush(numbers, int(input()))

rst = 0
while len(numbers) != 1:
    one = heapq.heappop(numbers)
    two = heapq.heappop(numbers)

    temp = one + two
    rst += temp
    heapq.heappush(numbers, temp)

print(rst)


# 단순 오름차순이 아님 - 반례: [20, 40, 50, 55, 70]
