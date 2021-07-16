import sys
from collections import deque
input = sys.stdin.readline


# 1. BFS를 사용한 탐색
def bfs(start_node, target_node):
    visited = {start_node: 0}
    q = deque([start_node])
    flag = False

    while q:
        now = q.popleft()

        if now == target_node:
            break

        # 1)
        next_node = now * 2
        if next_node not in visited and next_node <= target_node:
            q.append(next_node)
            visited[next_node] = visited[now] + 1
        # 2)
        next_node = now * 10 + 1
        if next_node not in visited and next_node <= target_node:
            q.append(next_node)
            visited[next_node] = visited[now] + 1

    # print(visited)
    if target_node not in visited:
        return -1

    return visited[target_node] + 1


# 2. target_node를 줄여 나가는 방식
def solve2(start_node, target_node):
    count = 0

    while target_node > start_node:
        if target_node % 10 == 1:
            target_node = (target_node - 1) // 10
            count += 1
        elif target_node % 2 == 0:
            target_node = target_node // 2
            count += 1
        else:
            break

    if start_node != target_node:
        return -1

    return count + 1


a, b = map(int, input().split())

print(bfs(a, b))
print(solve2(a, b))


"""
18. 16953 A→B (Silver 1)
    1.
    - 기본적인 bfs 완전 탐색 문제 start는 줄어드는 것 없이 계속 커지기 때문에 target보다 작거나 같은 경우에만
      탐색하는 것만 주의해주면 간단한 문제이다. 

    2.
    - 구글링을 통해서 start를 늘려가는 방법이 아닌 target을 줄이는 방법도 있다는 것을 알고 
      적용해 보았다. 
"""
