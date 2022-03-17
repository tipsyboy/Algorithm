ANSWER = 0
visited = []


def DFS(state, info, left, right, node_length) -> None:
    global ANSWER, visited

    # 방문 확인
    if visited[state]:  # 이미 이 상태는 확인함
        return
    visited[state] = True

    # 양/늑대 수 세기
    sheep = 0  # 양
    wolf = 0  # 늑대
    for i in range(node_length):
        if state & (1 << i):
            if info[i]:
                wolf += 1
            else:
                sheep += 1
    if sheep <= wolf:
        return

    # 양의 수 갱신
    ANSWER = max(ANSWER, sheep)

    # 다음 노드 찾기 (다음 경로 찾기)
    for i in range(node_length):
        if not (state & (1 << i)):  # 현재 상태에 가지고 있는 노드에서만 연결할 수 있으니까
            continue  # 안켜진 비트는 제외한다.

        if left[i] != -1:
            DFS(state | (1 << left[i]), info, left, right, node_length)
        if right[i] != -1:
            DFS(state | (1 << right[i]), info, left, right, node_length)


def solution(info, edges) -> int:
    global ANSWER, visited

    node_length = len(info)  # 노드 길이
    left = [-1] * node_length  # i번 노드의 왼쪽 자식
    right = [-1] * node_length  # i번 노드의 오른쪽 자식
    visited = [False] * (1 << node_length)  # visited[x]: x상태에 방문

    for u, v in edges:
        if left[u] == -1:
            left[u] = v
        else:
            right[u] = v

    DFS(1, info, left, right, node_length)

    return ANSWER


# info = [0, 1]
# edges = [[0, 1]]
# print(solution(info, edges))

info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
print(solution(info, edges))

"""
    - 양보다 늑대가 많거나 같아지면 안되면서, 이미 방문한 노드도 되돌아 가면서 양을 모을 수 있다. 
    
    - 즉, 노드만 정해지면 갈 수 있는 (양 > 늑대 경우의)경로가 정해지고 이때 max로 양을 얻을 수 있는 방법이 정해진다. 
    - 위와 같은 이유로 경로탐색에 집중하면서 path에 집중하는 것이 아니라 상태 state에 집중해서 봐야한다!!
    - 이 상태를 나타내는 값이 visited[]이고, 이미 탐색한 '상태'를 가지쳐주면서 효율적인 탐색이 가능하다. 
"""