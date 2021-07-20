import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline
MAX = 10 ** 5


def bfs(start, dest):
    if start >= dest:
        return start - dest

    pq = []
    heappush(pq, (0, start))
    visited = [False] * (MAX + 1)

    while pq:
        now_time, now_pos = heappop(pq)

        next_positions = [(now_time, now_pos * 2),
                          (now_time + 1, now_pos - 1),
                          (now_time + 1, now_pos + 1)]

        for nxt_time, nxt_pos in next_positions:
            if 0 <= nxt_pos <= MAX and not visited[nxt_pos]:
                if nxt_pos == dest:
                    return nxt_time  # return
                heappush(pq, (nxt_time, nxt_pos))
                visited[nxt_pos] = True


def bfs2(start, dest):
    if start >= dest:
        return start - dest

    q = deque([start])
    time = [-1] * (MAX + 1)
    time[start] = 0

    while q:
        now = q.popleft()

        # return
        if now == dest:
            return time[now]

        # 순간이동
        if 0 <= now * 2 <= MAX and time[now * 2] == -1:
            q.appendleft(now * 2)
            time[now * 2] = time[now]

        # 걷다
        next_positions = [now - 1, now + 1]
        for nxt in next_positions:
            if 0 <= nxt <= MAX and time[nxt] == -1:
                q.append(nxt)
                time[nxt] = time[now] + 1


start, dest = map(int, input().split())
print(bfs(start, dest))


"""
25. 13549 숨바꼭질3 (Gold 5)
    - bfs 문제이지만 특이 사항이 있다면, 순간이동의 경우에는 이전의 시간 값을 그대로 가져간다. 
      따라서 간선 값이 1로 고정된 경우가 아니고 0-1의 간선 값을 갖는 것이다. 

    1. 첫 번째 풀이
    - 이동 방식에 따라서 다른 시간 값을 가지고, 걷는 것보다 순간이동으로 다음 위치에 가는 것이 이득을 가지므로, 
      더 적은 거리를 갖는 값을 계속 뽑아내 줘야하고, 때문에 우선순위큐를 생각 하게 되었다.

      이렇게 하면 항상 순간이동으로 더 빠른 값을 갖는 경우가 앞에 오기 때문에 순간이동의 경우를 먼저 해결할 수 있었다.
      
      근데 틀렸었음,,, 중복 허용을 하지 않고, 시간 비교를 하지 않기 때문에 next_positions 탐색시 순간이동 값을 먼저
      계산해 줬어야 했다. -> 리스트 순서를 변경하고 바로 성공. (반례 1 2)

    2. 두 번째 풀이
    - 같은 방식의 bfs 풀이지만, 이번에는 기존과 같이 deque을 사용해서 풀었다. 
      순간이동의 경우에만 다른 결과를 가져오므로, 순간이동의 경우만 따로 계산해주고, 순간이동의 경우가 위와 같은 이유로
      먼저 계산을 해줘야 하므로 appendleft() 통해서 먼저 삽입한다. 
"""
