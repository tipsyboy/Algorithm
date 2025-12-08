# https://school.programmers.co.kr/learn/courses/30/lessons/340211

from collections import defaultdict


def solution(points, routes):
    risk = defaultdict(lambda: defaultdict(int))

    for route in routes:
        time = 0
        x, y = points[route[0] - 1]
        risk[time][(x, y)] += 1

        for nxt_pos in route[1:]:
            ex, ey = points[nxt_pos - 1]

            while x != ex or y != ey:
                if x != ex:
                    x = x + 1 if ex - x > 0 else x - 1
                elif y != ey:
                    y = y + 1 if ey - y > 0 else y - 1

                time += 1
                risk[time][(x, y)] += 1

    ans = sum(1 for time in risk for v in risk[time].values() if v > 1)
    return ans
