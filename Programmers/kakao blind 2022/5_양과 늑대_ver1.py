ANSWER = 0


def DFS(graph, sheep, wolf, cur, lands, info) -> None:
    """
    @param sheep - 양의 수
    @param wolf - 늑대 수
    @param cur - 현재 노드
    @param lands - 먹은 땅들
    @param info - 양/늑대 정보

    @return None, 전역 변경 로직
    """
    global ANSWER

    if info[cur]:
        wolf += 1
    else:
        sheep += 1

    if sheep <= wolf:
        return

    ANSWER = max(ANSWER, sheep)
    for land in lands:
        for adj in graph[land]:
            if adj not in lands:
                lands.add(adj)  # lands에 추가
                DFS(graph, sheep, wolf, adj, lands, info)  # DFS 탐색
                lands.remove(adj)  # lands에서 뺌

    return


def solution(info, edges) -> int:
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    lands = set()
    lands.add(0)

    DFS(graph, 0, 0, 0, lands, info)
    return ANSWER


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
print(solution(info, edges))