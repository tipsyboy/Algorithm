import sys

input = sys.stdin.readline


def floyd_warshall():
    n, m = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for _ in range(m):
        a, b, c = map(int, input().split())

        if graph[a - 1][b - 1] <= c:
            print("Enjoy other party")
        else:
            print("Stay here")


floyd_warshall()


"""
00. 11265 끝나지 않는 파티 (Silver 1)
    - 16~18 줄의 비교구문이 min() 함수를 사용할때는 TLE가 나고, 주석처리가 안된부분으로 사용하면 통과한다...
      같은 성능을 낸다고 생각했는데,, 아니었나.???

      왜 그러지??
"""