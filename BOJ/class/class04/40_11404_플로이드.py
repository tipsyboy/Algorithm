import sys

input = sys.stdin.readline
INF = int(1e9)


def floyd_warshall():
    # 자기 자신에게 가는 루트
    for i in range(1, n + 1):
        graph[i][i] = 0

    # Floyd_Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# graph 입력
for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a][b] = min(graph[a][b], c)  # a -> b의 비용이 c

floyd_warshall()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0, end=" ") if graph[i][j] >= INF else print(graph[i][j], end=" ")
    print()


"""
40. 11404 플로이드 (Gold 4)
    - 특이점 없는 Floyd-Washall 알고리즘 문제이다.
    
    - 문제 자체에 살짝 함정이 있는데, 
      a -> b를 가는 특정 노선이 여러개인 경우가 있는데, 이때, 비용 c를 비교하지 않고 graph에 추가하면 
      이후에 들어가는 값이 더 크더라도 더 큰 값으로 초기화 되기 때문에 graph에 경로를 추가할 때도 
      최소 값으로 초기화 하는 라인이 하나 더 필요하다.
"""