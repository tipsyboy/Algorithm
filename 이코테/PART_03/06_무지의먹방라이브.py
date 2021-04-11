import heapq


def solution(food_times, k):
    # 음식이 남지 않는 경우
    if sum(food_times) <= k:
        return -1

    q = []  # 최소 힙
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (food_time, 그릇 번호)

    sum_value = 0
    previous = 0
    length = len(food_times)

    # 이전 시간만큼 빼는게 결국 지나간 전체 시간만큼 빼는 것이 됨.
    while sum_value + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        # 이제 최소시간이 남은 접시의 시간 - 이전 접시 시간(이전접시 다먹은 시간만큼 흐름) * length
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])  # 음식 번호 기준 정렬

    return result[(k - sum_value) % length][1]


print(solution([3, 1, 2], 5))
