def rotate_arr_skin(query, graph) -> int:
    x1, y1, x2, y2 = query
    temp, minv = graph[x1 - 1][y1 - 1], graph[x1 - 1][y1 - 1]

    for i in range(x1 - 1, x2 - 1):  # 왼쪽
        graph[i][y1 - 1] = graph[i + 1][y1 - 1]
        minv = min(minv, graph[i + 1][y1 - 1])
    for i in range(y1 - 1, y2 - 1):  # 아래
        graph[x2 - 1][i] = graph[x2 - 1][i + 1]
        minv = min(minv, graph[x2 - 1][i + 1])
    for i in range(x2 - 1, x1 - 1, -1):  # 오른쪽
        graph[i][y2 - 1] = graph[i - 1][y2 - 1]
        minv = min(minv, graph[i - 1][y2 - 1])
    for i in range(y2 - 1, y1 - 1, -1):  # 위
        graph[x1 - 1][i] = graph[x1 - 1][i - 1]
        minv = min(minv, graph[x1 - 1][i - 1])
    graph[x1 - 1][y1] = temp  # 마지막꺼 옮겨줌

    return minv


def solution(rows, columns, queries) -> list:
    graph = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = num
            num += 1

    answer = []
    for query in queries:
        answer.append(rotate_arr_skin(query, graph))

    return answer


solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])


"""
    - 그냥 돌렸다.

    - 이런류의 문제가 많이 나오는 것 같다..?? 
"""