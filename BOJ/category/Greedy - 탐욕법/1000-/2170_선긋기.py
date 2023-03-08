# https://www.acmicpc.net/problem/2170

import sys

input = sys.stdin.readline

N = int(input())
queries = []
for _ in range(N):
    x, y = map(int, input().split())
    queries.append((x, y))
queries.sort(key=lambda x: (x[0], x[1]))

s, e = None, None
ans = 0
for query in queries:
    x, y = query
    if s == None and e == None:
        s, e = x, y
        continue

    if s < x <= e and y > e:
        e = y
    elif x > e:
        ans += e - s
        s, e = x, y

ans += e - s
print(ans)

"""
2170. 선 긋기
    - 현재 선분의 시작점과 끝점을 [s, e]라고 했을때, 다음 선분 [x, y]가 그려지는 상황은 총 5개가 된다. 
      앞으로 안겹침, s가 [x, y]사이, s, e 사이의 선분, e가 [x, y]의 중간, 뒤로 안겹침 (그려서 보면 편함)
      하지만, 선분들을 정렬한 후에 진행하면 1, 2번의 상황은 나타나지 않고 3번의 상황은 겹친 선분이 되므로 길이에 영향을 주지 않는다.
      따라서 4, 5번 상황만을 고려해서 4의 경우 선분을 늘려나가고 5의 경우 이전까지의 선분을 계산후 새로운 선분으로 계속 수행한다. 
"""