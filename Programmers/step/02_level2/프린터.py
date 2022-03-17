from collections import deque


def solution(priorities, location):
    q = deque([(i, p) for i, p in enumerate(priorities)])
    count = 1

    while q:
        if q[0][1] == max(q, key=lambda x: x[1])[1]:
            if q[0][0] == location:
                break

            q.popleft()
            count += 1
        else:
            q.append(q.popleft())

    return count


priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))
