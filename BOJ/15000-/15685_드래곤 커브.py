# 15685 드래곤 커브
import sys

input = sys.stdin.readline
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 동 북 서 남


def create_dragon_curve_on_graph(x, y, d, g) -> None:
    graph[y][x] = True
    move = [d]

    for i in range(g):
        for j in range(len(move) - 1, -1, -1):
            move.append((move[j] + 1) % 4)

    for m in move:
        ny, nx = y + directions[m][0], x + directions[m][1]

        if ny < 0 or ny > 100 or nx < 0 or nx > 100:
            continue
        graph[ny][nx] = True
        y, x = ny, nx


def checking_4_node() -> int:
    ans = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
                ans += 1

    return ans


N = int(input())
graph = [[False] * 101 for _ in range(101)]  # 격자의 크기 100*100
for _ in range(N):
    x, y, d, g = map(int, input().split())
    create_dragon_curve_on_graph(x, y, d, g)

print(checking_4_node())


"""
    15685. 드래곤 커브
    
    1. 문제 이해가 안되서 풀이를 깠는데, 평면 상의 x, y의 위치를 반대로 생각해서 였다. ㅜㅜ
       또한, 격자의 드래곤 커브로 생성되는 정사각형의 갯수를 세는 건줄 알고 한참 헤맸다..

    2. 평면 상의 꼭지점은 2차원 배열로 구성해주면 된다. graph[y][x] ==> (x, y)의 꼭지점을 지남.

    3. 다른 풀이에서는 규칙성이 생긴다고 했는데, 사실상 나중의 생긴 선분의 끝점이 회전시 축이 되고
       이때, 먼저 생긴 선분은 축으로 부터 멀리서 회전하게 되므로 당연한 결과임을 볼 수 있다. (규칙성이 생기는 것도 맞긴한듯...?)

"""