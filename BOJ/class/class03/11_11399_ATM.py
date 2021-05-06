# 1)
# n = int(input())
# times = list(map(int, input().split()))

# times.sort()

# rst = 0
# wait = 0

# for time in times:
#     wait += time
#     rst += wait

# print(rst)

# 2)
import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)  # heapify() 기존 list를 최소 힙구조로 변경
rst = 0
waiting = 0

for _ in range(n):
    waiting += heapq.heappop(heap)
    rst += waiting

print(rst)
