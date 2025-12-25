# https://www.acmicpc.net/problem/21608

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_like_and_blank(x: int, y: int, likes: list) -> tuple:
    like, blank = 0, 0
    for d in range(4):
        adj_x, adj_y = x + directions[d][0], y + directions[d][1]

        if adj_x < 0 or adj_x >= N or adj_y < 0 or adj_y >= N:
            continue

        if seat[adj_x][adj_y] in likes:
            like += 1
        elif seat[adj_x][adj_y] == 0:
            blank += 1

    return (like, blank)


def set_seat(s_num: int, likes: list) -> None:
    max_like = 0
    pq = []
    for i in range(N):
        for j in range(N):

            if seat[i][j]:
                continue

            like, blank = get_like_and_blank(i, j, likes)
            if like > max_like:
                pq = []
                heappush(pq, (-blank, i, j))
                max_like = like
            elif like == max_like:
                heappush(pq, (-blank, i, j))

    _, x, y = heappop(pq)
    seat[x][y] = s_num


def good_score() -> int:
    ans = 0
    for i in range(N):
        for j in range(N):
            like, _ = get_like_and_blank(i, j, like_table[seat[i][j]])

            if like == 1:
                ans += 1
            elif like == 2:
                ans += 10
            elif like == 3:
                ans += 100
            elif like == 4:
                ans += 1000

    return ans


N = int(input())
like_table = [[] for _ in range(N ** 2 + 1)]
seat = [[0] * N for _ in range(N)]
for _ in range(N ** 2):
    s, *likes = map(int, input().split())
    set_seat(s, likes)

    like_table[s] = likes

print(good_score())

"""
21608. 상어 초등학교
    - 상어 구현 입문

    - 크게 어렵지 않음
    
    - 이런류의 문제는 초반에 시간이 좀 더 들더라도 문제를 꼼꼼히 읽고 제시하는 방향을 전부 정리한 후에 접근 하는게 좋은 것 같다.
      코드를 재활용 할 수 있는 부분도 더러 있고, 
      무엇보다 그냥 대충 시작했다가 중간에 길을 잃었을 때, 시간이 두배/세배 또는 아예 못풀어서 전부 밀고 다시 작성해야 하는 경우도 생김
"""