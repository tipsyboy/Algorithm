import sys
import heapq
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    min_heap, max_heap = [], []
    visited = [False] * 1_000_001

    command_num = int(input())
    for key in range(command_num):
        command = input().split()

        if command[0] == "I":
            heapq.heappush(min_heap, (int(command[1]), key))
            heapq.heappush(max_heap, (int(command[1]) * -1, key))
            visited[key] = True

        elif command[0] == "D":
            if command[1] == "-1":
                # 현재 heap의 최상단 노드(다음 pop 순위)의 키의 visited값이 false이면 이미 다른 heap에서 나간 것
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)  # 때문에 빼줌
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif command[1] == "1":
                while max_heap and not visited[max_heap[0][1]]:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    # 쓰레기 값 처리
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(max_heap[0][0] * -1, min_heap[0][0])
    else:
        print("EMPTY")


"""
44. 7662 이중 우선순위 큐 (gold 5)
    - MAX heap과 min heap의 연결을 어떻게 할 것인가..?
"""
