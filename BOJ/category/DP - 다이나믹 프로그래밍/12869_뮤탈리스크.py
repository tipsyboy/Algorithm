# https://www.acmicpc.net/problem/12869
# 2022-08-13 Sat

import sys
from collections import deque

input = sys.stdin.readline
ATT_COMBI = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
INF = float("inf")


def attack(N: int, SCVs: list) -> int:
    q = deque([tuple(sorted(SCVs))])
    vis = dict()
    vis[tuple(sorted(SCVs))] = 0
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            now = q.popleft()
            for i in range(6):
                temp = [0] * N
                for j in range(N):
                    if now[j] - ATT_COMBI[i][j] > 0:
                        temp[j] = now[j] - ATT_COMBI[i][j]

                nxt = tuple(sorted(temp))
                if nxt in vis:
                    continue
                q.append(nxt)
                vis[nxt] = cnt

    return vis[tuple([0] * N)]


N = int(input())
SCVs = list(map(int, input().split()))
print(attack(N, SCVs))


"""
12869. 뮤탈리스크
    - bfs + dp
    - SCV의 최대 개수가 3개이고, 매번 남은 SCV들의 체력 상황을 저장하면서 해결했다. 

    - 3차원 dp로 해결한 방법이 있던데 추후에 추가할 예정
"""