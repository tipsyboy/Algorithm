# https://school.programmers.co.kr/learn/courses/30/lessons/340211

from collections import deque, defaultdict


def collision(risk):
    rst = 0
    for v in risk.values():
        if v > 1:
            rst += 1
    return rst


def move(cur, dest):
    x, y = cur
    ex, ey = dest

    if x != ex:
        x = x + 1 if ex - x > 0 else x - 1
    elif y != ey:
        y = y + 1 if ey - y > 0 else y - 1

    return (x, y)


def solution(points, routes):
    q = deque()
    risk = defaultdict(int)
    for route in routes:
        cur, *via = map(lambda x: int(x) - 1, route)
        cur = tuple(points[cur])
        dest = tuple(points[via[0]])
        nxt = via[1:][::-1]
        q.append((cur, dest, nxt))
        risk[cur] += 1
    ans = collision(risk)

    while q:
        risk = defaultdict(int)
        for _ in range(len(q)):
            cur, dest, nxt_dest = q.popleft()
            nxt = move(cur, dest)
            risk[nxt] += 1

            if nxt != dest:
                q.append((nxt, dest, nxt_dest))
            elif nxt == dest and nxt_dest:
                q.append((nxt, tuple(points[nxt_dest.pop()]), nxt_dest))

        ans += collision(risk)

    return ans


print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))
