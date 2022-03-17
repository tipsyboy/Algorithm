from heapq import heappush, heappop, heapify


def solution(scoville, K):
    heapify(scoville)
    count = 0

    while len(scoville) > 1 and scoville[0] < K:
        a = heappop(scoville)
        b = heappop(scoville)

        heappush(scoville, a + b * 2)
        count += 1

    if scoville[0] < K:
        return -1

    return count


K = 7
scoville = [1, 2, 3, 9, 10, 12]
print(solution(scoville, K))