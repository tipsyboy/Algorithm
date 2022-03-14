import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution():
    count = 0
    for _ in range(t):
        if pq[0] * -1 < h:
            break

        x = (heappop(pq) * -1) // 2
        if x < 1:
            x = 1

        heappush(pq, x * -1)
        count += 1

    if pq[0] * -1 < h:
        return count
    else:
        return -1


n, h, t = map(int, input().split())
pq = []
for _ in range(n):
    x = int(input())
    heappush(pq, x * -1)

rst = solution()
if rst == -1:
    print("NO")
    print(pq[0] * -1)
else:
    print("YES")
    print(rst)
