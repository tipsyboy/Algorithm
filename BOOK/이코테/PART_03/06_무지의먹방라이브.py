import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution(food_times, k):
    # 모든 음식 수보다 시간이 같거나 더 주어지면 다 먹음
    if sum(food_times) <= k:
        return -1

    pq = []  # 우선순위 큐
    dish = len(food_times)  # 접시의 총 개수
    time = 0  # 지난 시간
    prev_dish = 0  # 이전 접시에 있던 음식 양

    for i in range(dish):
        heappush(pq, (food_times[i], i + 1))  # 음식 양, 접시 번호

    # 음식이 가장 적은 접시를 시간 내에 다 먹을 수 있을때까지
    while time + (pq[0][0] - prev_dish) * dish <= k:
        now_dish = heappop(pq)[0]  # 다 먹을 수 있으면, 현재 접시의 음식을 모두 꺼냄

        # 한 접시를 1s 동안 먹고, 다음으로 넘기므로 현재 접시의 음식을 다 먹으려면 접시의 음식만큼 순회해야함
        time += (now_dish - prev_dish) * dish  # 다 먹는 시간 만큼 time에 추가
        prev_dish = now_dish  # 계산을 위해 이전 접시 갱신
        dish -= 1  # 이번 음식을 다 먹었으므로 접시 하나 뺌

    # 남은 시간을 처리하기 위해서 접시 번호 순서대로 정렬
    pq.sort(key=lambda x: x[1])

    # 남은 시간에서 지난 시간 만큼 뺀 시간만큼 음식을 더 먹을 수 있다.
    return pq[(k - time) % dish][1]


print(solution([3, 1, 2], 5))
