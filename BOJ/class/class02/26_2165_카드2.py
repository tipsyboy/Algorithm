from collections import deque

n = int(input())

queue = deque([x for x in range(1, n+1)])

while len(queue) > 1:
    queue.popleft()
    # print(queue)
    queue.append(queue.popleft())
    # print(queue)

print(queue[-1])
