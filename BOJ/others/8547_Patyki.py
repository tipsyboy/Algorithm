from heapq import heappush, heappop, heapify

n = int(input())
pq = list(map(int, input().split()))
heapify(pq)
count = 0

while len(pq) > 1:
    a = heappop(pq)
    b = heappop(pq)

    if a != b:
        count += 1
        heappush(pq, b)
    else:
        heappush(pq, a + b)

    # print(pq)

print(len(pq) + count)


"""
solved 우선순위큐 검색해서 품 - etc

"""