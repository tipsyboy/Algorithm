import sys

input = sys.stdin.readline

n, m = map(int, input().split())
staff = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(n):
    if staff[i] == -1:
        continue
    graph[staff[i]].append(i + 1)

ans = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    ans[i] += w


stack = [(1, 0)]
visited = [False] * (n + 1)
while stack:
    now, w = stack.pop()
    visited[now] = True
    ans[now] += w

    for adj in graph[now]:
        if visited[adj]:
            continue
        stack.append((adj, ans[now]))
print(*ans[1:])


"""
14267. 회사 문화 1
    - 첫 번째 시도 (WA)
      한 상사에 따른 직속 부하가 한 명이라고 생각해서, 리버스 배열만 가지고 풀었음 
      당연히 틀렸고 내가 멍청한게 맞긴 한데, 직속 부하라고 해서 속음 ㅋㅋ..

    - 두 번째 시도 (TLE)
      매 쿼리마다 업데이트 했고 당연히 TLE 였음.

    - 세 번째 (AC)
      쿼리를 먼저 입력 받고 ans를 초기화 해준 다음 
      dfs를 한꺼번에 돌아서 ans를 업데이트 해줬음. 
"""