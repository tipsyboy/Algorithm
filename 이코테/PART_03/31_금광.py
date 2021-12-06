import sys

input = sys.stdin.readline


def solution(gold):
    graph = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            graph[i][j] = gold[i * m + j]

    # print(graph)
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                graph[i][j] = max(graph[0][j - 1], graph[1][j - 1]) + graph[i][j]
            elif i == n - 1:
                graph[i][j] = max(graph[i][j - 1], graph[i - 1][j - 1]) + graph[i][j]
            else:
                graph[i][j] = max(graph[i][j - 1], graph[i - 1][j - 1], graph[i + 1][j - 1]) + graph[i][j]

    # print(graph)
    rst = 0
    for i in range(n):
        rst = max(rst, graph[i][m - 1])

    return rst


tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))

    print(solution(gold))


"""
# test case

2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""