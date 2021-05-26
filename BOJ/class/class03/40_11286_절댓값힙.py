import sys
import heapq
input = sys.stdin.readline


n = int(input())
heap = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))


"""
40. 11286 절댓값 힙 (silver 1)
    - 튜플로 저장하면 heap의 0번째 원소에 대해서 정렬하므로 입력된 값(num)의 절댓 값을 튜플의
      0번 원소로 저장하고 1번 원소에 원래 값을 저장해서 해결한다. 
    
    - 단순히 이 문제를 푸는 것만이 아니라 heap에 저장 값을 위와 같이 여러개를 사용하면서
      다른 문제들에 사용할 수 있을 것 같다. (구현문제라던지)
    
    - heap 자료구조에 대해서 다시 공부하고, class를 이용해서 구현해 볼 것
"""
