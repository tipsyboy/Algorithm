import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())  # 뱀의 수, 사다리의 수
snakes_ladders = dict()  # 뱀과 사다리 저장

# 뱀과 사다리 입력
for _ in range(n + m):
    a, b = map(int, input().split())
    snakes_ladders[a] = b

visited = [0 for _ in range(101)]
q = deque()
q.append(1)

while q:
    now = q.popleft()

    for i in range(1, 7):
        next_node = now + i

        if next_node > 100:
            continue

        if next_node in snakes_ladders:
            next_node = snakes_ladders[next_node]

        if not visited[next_node]:
            q.append(next_node)
            visited[next_node] = visited[now] + 1

# print(snakes_ladders)
# print(visited)
print(visited[100])


"""
42. 16928 뱀과 사다리 게임 (silver 1)
    - 이전 위치에서 다음 위치로 이동하는데, 비용이 1로 고정된 문제로 (1회의 주사위 던짐을 사용)
      bfs를 사용해서 찾아낼 수 있는 문제였다.

    - 뱀과 사다리의 위치에 도착하면 무조건 지정된 위치로 이동하기 때문에, next_node를 
      미리 결정해서 방문여부를 검증한다. 이미 방문한 노드는 이미 최소 이동을 거친점이기 때문에
      검증하지 않는다. 

    - 상황에 따라서 뱀을 밟는게 더 유리한 경우도 있지만, 뱀과 사다리가 한 노드에 같이 존재할 수 없기 때문에
      뱀과 사다리의 위치를 한꺼번에 snakes_ladders dict에 저장해서 해결했다. 

    - 처음에 실패했던 문제로, 반례를 찾아보니 사다리를 탔을 때, 100의 위치로 가는 경우를 생각하지 않고
      visited[]를 100개만 생성해서 문제를 풀다보니 틀렸었다. (0번 index를 1로 생각하고) 
      배열 길이만 101까지로 늘려주니 바로 성공했다. 
"""
