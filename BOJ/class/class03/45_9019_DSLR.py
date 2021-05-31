import sys
from collections import deque
input = sys.stdin.readline


# 왼쪽으로 숫자열을 회전
def rotate_L(num):
    front = num % 1000
    back = num // 1000

    return front * 10 + back


# 오른쪽으로 숫자열을 회전
def rotate_R(num):
    front = num % 10
    back = num // 10

    return front * 1000 + back


# bfs
def bfs(start, target):
    q = deque([start])
    visited = ["" for _ in range(10000)]

    while q:
        now = q.popleft()

        # D 연산
        # 현재 node가 0인 경우 D연산을 하지 않는다.
        if now != 0:
            d = (now * 2) % 10000
            if visited[d] == "":
                q.append(d)
                visited[d] = visited[now] + "D"

        # S 연산
        s = (now - 1) if now != 0 else 9999  # 현재 노드가 0인 경우 -1이 되므로 9999
        if visited[s] == "":
            q.append(s)
            visited[s] = visited[now] + "S"

        # L 연산
        l = rotate_L(now)  # 숫자열을 왼쪽으로 회전
        if visited[l] == "":
            q.append(l)
            visited[l] = visited[now] + "L"

        # R 연산
        r = rotate_R(now)  # 숫자열을 오른쪽으로 회전
        if visited[r] == "":
            q.append(r)
            visited[r] = visited[now] + "R"

        # target 확인
        if visited[target] != "":
            break

    return visited[target]


t = int(input())

for _ in range(t):
    start, target = map(int, input().split())

    print(bfs(start, target))


"""
45. 9019 DSLR (Gold 5)
    - 이전에 풀었던 문제들과 비슷한 유형이라고 생각해서 bfs로 풀어야 한다는 것은
      바로 알 수 있었다.

    - 그런데 정~~~말 많이 실패함. 
      1) 처음에는 S연산에서 0 -> -1 내려가는 구간에서 런타임 에러가 자꾸 나서 실패했고,
      2) rotate 연산에서 str으로 캐스팅해서 이동후 다시 int로 캐스팅 했는데, 이 과정에서 계속 시간초과가 났다. 
      3) D연산에서 현재 node가 0번인 경우 그대로 0이 되는데, 이때 결과값인 visited[0]이 비어있는 경우 
         의미 없이 D연산만 추가되는 결과를 가져옴
    
    - 위의 문제들을 하나하나씩 해결하면서 문제를 풀었다. 다만, pypy3으로 통과 했는데, 결과를 보니까 
      python3로 통과한 사람들은 3명 밖에 없어서 약간 허탈했다. (4번 통과에 한명 중복)

    - 문제 풀이가 좀 익숙해지긴 했는데, 아직 생각한 알고리즘을 구현하는 과정에서 막히는 부분이 있는 것 같다.
"""
