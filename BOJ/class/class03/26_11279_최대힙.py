import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    temp = int(input())

    if temp != 0:
        heapq.heappush(heap, (-temp, temp))
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)


"""
    파이썬은 최소 힙만을 라이브러리로 제공한다. 
    따라서 최대 힙을 사용하려면 약간의 테크닉을 사용해서 사용하는데,
    *(-1)을 해서 최소 힙에 저장하는 방법이 있다.
    위 코드에서는 *(-1)을 한것과 원래 값을 튜플로 저장해서 힙큐에 추가했다

    class와 node를 통해서 트리 구조에 대해서 구현해 볼 것. 
"""
