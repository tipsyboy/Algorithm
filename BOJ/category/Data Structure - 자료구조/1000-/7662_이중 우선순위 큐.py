# https://www.acmicpc.net/problem/7662

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    Q = int(input())
    visited = [False] * Q
    min_heap = []
    max_heap = []

    for i in range(Q):
        command, item = input().split()

        if command == "I":
            item = int(item)
            heappush(min_heap, (item, i))
            heappush(max_heap, (item * -1, i))
        elif command == "D":
            if item == "-1":
                while min_heap and visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    __, key = heappop(min_heap)
                    visited[key] = True
            elif item == "1":
                while max_heap and visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    __, key = heappop(max_heap)
                    visited[key] = True

    while min_heap and visited[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]:
        heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
