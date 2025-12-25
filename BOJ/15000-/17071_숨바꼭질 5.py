# Dec 4, Thu 2025
# https://www.acmicpc.net/problem/17071

import sys
from collections import deque

input = sys.stdin.readline
MX = 5 * (10**5)


def bfs(N, K):
    if N == K:
        return 0

    visited = [[False] * 2 for _ in range(MX + 1)]  # 홀/짝수 시간
    visited[N][0] = True  # 최초 수빈이의 위치
    q = deque([N])

    time = 1
    while q:
        K += time
        if K > MX:
            return -1
        for _ in range(len(q)):
            cur = q.popleft()
            for d in [-1, 1, cur]:
                nxt = cur + d

                if nxt < 0 or nxt > MX:
                    continue
                if visited[nxt][time & 1]:
                    continue

                visited[nxt][time & 1] = True
                q.append(nxt)

        if visited[K][time & 1]:
            return time

        time += 1

    return -1


N, K = map(int, input().split())
print(bfs(N, K))


"""
17071. 숨바꼭질 5

1. 
수빈이가 t1초에 x의 위치에 도착했다고 하자.
규칙에 따라 수빈이는 t1+2, t1+4, t1+6 ... t1+2n초에 x위치에 존재할 수 있다. 
따라서 2초의 시간을 들여 무한 와리가리를 하면 잡을 수 있음. 

2. 
bfs를 사용해서 수빈이가 먼저 훑고 간 지역에 동생이 도착한다면 무한 와리가리 대기를 통해서 잡을 수 있다. 
따라서 수빈이가 이미 지난 좌표는 방문 체크를 하고 동생이 그 위치에 도착한다면 그 시간이 답이됨.

3. 
다만 수빈이가 x의 위치에서 다시 x의 위치로 돌아오려면 2n초가 걸리므로 방문 체크를 홀/짝수 시간으로 나눠서 구분한다. 

"""
