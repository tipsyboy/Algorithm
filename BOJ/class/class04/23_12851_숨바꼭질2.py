import sys
from collections import deque
input = sys.stdin.readline
MAX = 10**5


def bfs1(start, dest):
    if start >= dest:
        return start - dest, 1

    dist = [-1] * (MAX + 1)
    q = deque([start])
    dist[start] = 0
    count = 0

    while q:
        now = q.popleft()

        if now == dest:
            count += 1

        next_positions = [now - 1, now + 1, now * 2]
        for nxt in next_positions:
            if 0 <= nxt <= MAX:
                # next node를 방문하지 않았거나 / 방문했으면 최단 루트로
                if dist[nxt] == -1 or dist[nxt] == dist[now] + 1:
                    # 목적지까지 이미 도달한 경우(최단거리를 찾았음) 더 짧은 루트가 아니라면 스킵한다(최단거리가 아니면)
                    if dist[dest] != -1 and dist[nxt] < dist[now] + 1:
                        continue
                    q.append(nxt)
                    dist[nxt] = dist[now] + 1

    return dist[dest], count


def bfs2(start, dest):
    #
    if start >= dest:
        return start - dest, 1

    dist = [-1] * (MAX + 1)
    q = deque([start])
    dist[start] = 0
    count = 0
    flag = False

    while q:
        q_length = len(q)

        for _ in range(q_length):
            now = q.popleft()

            next_positions = [now - 1, now + 1, now * 2]
            for nxt in next_positions:
                if 0 <= nxt <= MAX:
                    if dist[nxt] == -1 or dist[now] + 1 == dist[nxt]:
                        q.append(nxt)
                        dist[nxt] = dist[now] + 1

                    if nxt == dest:
                        count += 1
                        flag = True

        if flag:
            break

    return dist[dest], count


start, dest = map(int, input().split())
# rst_time, rst_count = bfs1(start, dest)
rst_time, rst_count = bfs2(start, dest)
print(rst_time)
print(rst_count)


"""
23. 12851 숨바꼭질2 (Gold 5)
    1. 처음 생각
    - bfs를 통해서 최단거리를 찾고, 찾은 최단거리를 통해서 backtracking 해서 루트를 찾으려고 했으나, 
      조금 더 생각해보니까 좋은 방법이 아니라고 생각되어서 그만 두었다. 
    
    2.
    - bfs에 조건 넣기
      숨바꼭질2는 전형적인 bfs + bfs에 조건넣기를 사용하는 숨바꼭질 시리즈 중 하나이다. 
      목적지까지 도달하는 모든 방법을 찾아야 하므로 이미 방문한 점도 포함할 수 있다. 노드 도달 중복이 가능한 것
      때문에 무한루프를 돌지 않게 하기 위해서 종료조건과 count를 셀 방법을 찾아야한다.
      사실은 범위가 10만까지의 범위고 dest에 도달하는 조건만 넣어줘도 완전 탐색을 통해서 2s안에 문제를 해결할 수는 있다. (600ms 정도 나오는 듯)

      but, 조건을 넣어주면서 조금 더 빠르고 정확하게 찾아보자. 

    3. 
    - 1) 두 방법 모두 처음에 start >= dest인 경우의 예외처리를 해줬다. 
      문제상으로 뒤로 갈 수 있는 방법은 -1 하나뿐이므로, dest까지 계속 -1 해주는 방법이 최단거리 방법이 되고 당연히 한가지 방법이다. 

    - 2) 이제 조건을 주는데, 
        1 - 첫째로 범위 안의 수여야 하며, 
        2 - 처음 방문한 경우와 / 두번 이상 방문 하는 경우를 둘다 알아야한다. 
            첫 방문의 경우 당연하게도 dist[]의 값이 초기값일 것이고, 
            두 번 이상 방문하는 경우에는 현재 노드에 + 1을 값이 다음 노드의 이미 저장된 값보다 작거나 같은 경우가 아니면, 
            이 루트는 최단거리의 루트가 아니라는 것이다. (사실 bfs는 첫 탐색에 이미 최단거리를 찾아낸다.)
        3 - 다음 조건은 노드간 거쳐가는 최단거리를 찾다가 목적지의 최단거리를 찾은 이후인데, 이때부터는 각 노드에 저장된 
            최단거리보다 현재 노드의 거리 + 1의 값이 더 큰 경우는 마찬가지로 최단거리가 아니므로 갈 필요가 없다. 
            따라서, 제외해주고 deque에 값을 저장하는 방식으로 가주면 된다. 

    4. 두 번째 방법
    - 1) 이전에 풀었던 아기 상어와 같은 방식으로 현재 q에 저장된 모든 노드를 전부 확인 하는 방법을 사용한다.
         이 방법이 처음에는 굉장히 이질감이 들었었는데, bfs는 계층적으로 다음 단계로 넘어가면서 탐색을 하는데,
         추상적으로 q를 탐색하는 것보다 좀 더 구체적/직관적인 방식이며 더더욱 빠르다.
         
         bfs답게 완전탐색의 방식이지만, 현재 계층에서(이 문제에서 계층은 시간 1s에 갈 수 있는 노드 2s갈 수 있는 노드....)
         가능한 모든 노드를 전부 탐색하므로써 목적지 계층에 도착한 이후에는 탐색하지 않는다. 
         따라서 탐색 노드의 범위가 다른 방법들보다 더 적으며 좀 더 직관적으로 이해할 수 있다.

         익숙해지기 필수다.  
"""
