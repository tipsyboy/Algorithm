INF = float("inf")


def floyd_warshall(n: int, s: int, a: int, b: int, fares: list) -> list:
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0

    for u, v, fare in fares:
        graph[u][v] = fare
        graph[v][u] = fare

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # 1) 느림 -> min객체 생성

    return graph


def solution(n: int, s: int, a: int, b: int, fares: list) -> int:
    graph = floyd_warshall(n, s, a, b, fares)

    fare = graph[s][a] + graph[s][b]
    for i in range(1, n + 1):
        fare = min(fare, graph[s][i] + graph[i][a] + graph[i][b])

    return fare


"""
4. 합승 택시 요금
    - 이게 3번으로 나온 문제보다 훨씬 쉽다... 난이도가 어떻게 된건지 

    - 플로이드-와샬로 함
"""