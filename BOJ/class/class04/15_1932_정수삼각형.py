import sys
input = sys.stdin.readline


def solve(n, graph):
    # if n == 1:
    #     return graph[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                graph[i][j] = graph[i-1][j] + graph[i][j]
            elif j == i:
                graph[i][j] = graph[i-1][j-1] + graph[i][j]
            else:
                graph[i][j] = max(graph[i-1][j-1], graph[i-1][j]) + graph[i][j]

    # print(graph)
    return max(graph[n-1])


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(solve(n, graph))


"""
15. 1932 정수 삼각형 (Silver 1)
    - 간단한 DP문제 
      현재 항 i에서 열 값이 0 or i==j인 경우는 선택할 가짓수가 없으므로 그냥 더해주고
      위와 같은 경우가 아닐땐, 이전 항의 더할수 있는 수 2가지를 놓고 큰 값을 선택해주면 된다. 
    
    - 특히, 파이썬의 경우 index만 주의해주면 간단하게 풀 수 있었다.
"""
