from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque(truck_weights)
    on_bridge = deque()
    all_weights = 0

    while q or on_bridge:
        # 다리에서 내리기
        while on_bridge and time - on_bridge[0][1] == bridge_length:
            all_weights -= on_bridge[0][0]
            on_bridge.popleft()

        # 다리 타기
        if q and all_weights + q[0] <= weight:
            all_weights += q[0]
            on_bridge.append((q.popleft(), time))

        time += 1

    return time


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
solution(bridge_length, weight, truck_weights)