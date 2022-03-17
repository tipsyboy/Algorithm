from heapq import heappush, heappop


def solution(operations):
    length = len(operations)
    visited = [False] * length
    max_heap, min_heap = [], []

    for i in range(length):
        command, value = operations[i].split()

        if command == "I":
            heappush(max_heap, (int(value) * -1, i))
            heappush(min_heap, (int(value), i))
            visited[i] = True
        elif command == "D":
            if value == "1":  # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
            elif value == "-1":  # 최소값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)

    # 쓰레기 값 처리
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)

    if not max_heap and not min_heap:
        return [0, 0]

    return [-1 * max_heap[0][0], min_heap[0][0]]


operations = ["I 7", "I 5", "I -5", "D -1"]
print(solution(operations))
