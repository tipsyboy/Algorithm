import sys

input = sys.stdin.readline
INF = int(1e9)


def floyd_warshall():
    for i in range(1, n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    count = 0
    for i in range(1, n + 1):
        flag = True
        for j in range(1, n + 1):
            if graph[i][j] == INF and graph[j][i] == INF:
                flag = False
                break

        if flag:
            count += 1

    return count


n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a][b] = 1

print(floyd_warshall())

"""
38. 정확한 순위 (part 3)
    - 특정 학생 a가 가리키는 대상은 a보다 성적이 높은 학생이다. 

    - 이때, 가리키는 대상 학생을 b라고 하면 성적이 같은 경우는 없으므로, b -> a 인 경우는 (양방향) 불가능하다.

    - 때문에 a가 가리키고 있지 않은 학생 c가 a를 가리키고 있다면, a의 순위는 c와 b사이로 특정된다. 
      (a -> b), (a -> c: INF, c -> a: not INF)
    
    - 따라서, 플로이드-워셜 알고리즘을 통해서 위의 경우를 찾아주면 특정되는 학생의 수를 찾을 수 있다.  
"""