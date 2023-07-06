# https://www.acmicpc.net/problem/2932

"""
2932. 표 회전
    - 처음에는 실제 표를 만들어서 표의 이동을 통해서 해결하려고 했고 MLE를 받음
      표의 크기가 N(2 <= N <= 10000)으로 4*N*N 하면 400MB 정도 되므로 MLE

    - 때문에 표를 만들지 않고 해결해야 함
    
    - 1. 표의 숫자들은 순서대로 써져 있어 초기 위치를 찾을 수 있으므로 
      2. 각 명령에 대해서 이동 값만 prev에 저장하고 매 쿼리마다 타깃의 초기위치 (ox, oy)에서 
      3. prev[]의 이전 명령을 수행한 현재 위치를 찾고 현재 위치에 대해서 이번 쿼리를 수행 후
      4. 다시 prev[]에 이번 쿼리의 명령을 저장한다. 

    - 내 풀이가 정해인지는 모르겠으나, 난이도가 S2보다는 높게 설정되야 할 거같은데 모르겠다. 
      난 G4줬음
"""


import sys

input = sys.stdin.readline


def get_og_coord(X: int) -> tuple:
    """
    - 수 X의 초기 위치를 찾는다.
    """

    q, r = divmod(X, N)
    if r == 0:
        return (q - 1, N - 1)

    return (q, r - 1)


def move_cur_to_next(cx: int, cy: int, tx: int, ty: int) -> int:
    """
    - 이동에 필요한 회전 수를 찾는다.
    """

    my = N - cy + ty if cy > ty else ty - cy
    mx = N - cx + tx if cx > tx else tx - cx

    prev.append([cx, my, ty, mx])
    return mx + my


def get_cur_coord(x: int, y: int) -> tuple:
    """
    - 수 X의 원래 위치 (ox, oy)에서 이전에 이동했던 prev[]의 이동에 따라 현재 수 X가 어디있는지 찾는다.
    """

    cur_x, cur_y = x, y
    for a, b, c, d in prev:  # a행이 b, c열이 d 만큼 이동
        # print("(%d, %d) -> " % (cur_x, cur_y), end=" ")
        if cur_x == a:
            cur_y = (cur_y + b) % N
        if cur_y == c:
            cur_x = (cur_x + d) % N
        # print("(%d, %d)" % (cur_x, cur_y))

    return (cur_x, cur_y)


N, K = map(int, input().split())
prev = []
for _ in range(K):
    X, R, C = map(int, input().split())

    ox, oy = get_og_coord(X)  # og x, og y
    cx, cy = get_cur_coord(ox, oy)
    print(move_cur_to_next(cx, cy, R - 1, C - 1))  # cur x, cur y, target x, target y
