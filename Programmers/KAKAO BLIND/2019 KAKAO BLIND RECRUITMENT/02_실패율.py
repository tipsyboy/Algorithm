# https://school.programmers.co.kr/learn/courses/30/lessons/42889

from collections import defaultdict


def solution(N, stages):
    fails = defaultdict(int)
    for stage in stages:
        fails[stage] += 1

    total = len(stages)
    fail_rates = defaultdict(float)
    for i in range(1, N + 1):
        fail_rates[i] = 0
        if total != 0:
            fail_rates[i] = fails[i] / total
            total -= fails[i]

    sorted_fail_rates = sorted(fail_rates.items(), key=lambda x: (-x[1], x[0]))
    ans = [x[0] for x in sorted_fail_rates]

    return ans


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))

"""
실패율

문제의 포인트
1. 문제 조건의 이해
    - stages[i] = 4, 현재 3까지 깼다.
    - 실패율 = 도달했으나 깨지 못함 / 도달한 플레이어 수 
    - stages[i] <= N + 1
2. 헤매이지 않고 쭉 풀어나갈 수 있는가? << 이게 초반 문제들은 중요함. 잘 정리하고 문제로 들어가는 것이 중요
3. total == 0인 경우 분모가 0이 되기 때문에 이 경우를 골라낼 수 있는가? << 중요 / 항상 불능인 경우

---
- 수학
- 브루트 포스
- 자료구조
"""
