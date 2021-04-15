from collections import deque
from itertools import permutations


def solution(n, weak, dist):
    rst = len(dist) + 1  # 가장 적은 수의 친구를 투입하는 수를 찾아야 하기 때문에 최대 친구수보다 하나 많은 것으로 초기화
    weak_que = deque(weak)
    for _ in range(len(weak)):
        for friends in permutations(dist, len(dist)):
            start = weak_que[0]
            count = 1  # 현재 투입된 친구
            # 모든 취약 지점을 검사
            for i in range(len(weak)):
                if start + friends[count - 1] < weak_que[i]:  # 지금 갈 수 없는 거리임
                    count += 1  # 새 친구 투입
                    if count > len(dist):
                        break
                    start = weak_que[i]  # 현재 검사 했을때, 못가는 곳을 다시 출발지점으로 지정
                    # 새 친구가 남았는지 검사
            rst = min(rst, count)

        weak_que.append(weak_que.popleft() + n)

    if rst > len(dist):
        return -1

    return rst


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
