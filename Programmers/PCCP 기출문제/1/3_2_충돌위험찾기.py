# https://school.programmers.co.kr/learn/courses/30/lessons/340211

from collections import defaultdict


def move(cur, dest):
    x, y = cur
    ex, ey = dest

    if x != ex:
        x = x + 1 if ex - x > 0 else x - 1
    elif y != ey:
        y = y + 1 if ey - y > 0 else y - 1

    return (x, y)


def solution(points, routes):
    risk = defaultdict(lambda: defaultdict(int))

    for route in routes:
        time = 0
        cur = tuple(points[route[0] - 1])
        risk[time][cur] += 1

        for nxt_pos in route[1:]:
            dest = tuple(points[nxt_pos - 1])
            while cur != dest:
                cur = move(cur, dest)
                time += 1
                risk[time][cur] += 1

    ans = 0
    for time in risk.keys():
        for v in risk[time].values():
            if v > 1:
                ans += 1

    return ans


print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))
