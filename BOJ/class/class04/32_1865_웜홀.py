import sys

input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(start):
    dist = [INF] * (n + 1)
    # dist[start] = 0

    for i in range(n):  # 모든 노드
        for edge in edges:
            now_node, nxt_node, cost = edge

            if dist[nxt_node] > dist[now_node] + cost:
                dist[nxt_node] = dist[now_node] + cost  # 갱신

                if i == n - 1:
                    return True

    return False


t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())

    # 간선
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        # undigraph
        edges.append((a, b, c))
        edges.append((b, a, c))

    for _ in range(w):
        a, b, c = map(int, input().split())

        edges.append((a, b, -c))  # direct

    if bellman_ford(1):
        print("YES")
    else:
        print("NO")


"""
32. 1865 웜홀 (Gold 4)
    - Dijkstra 알고리즘을 공부하다가 만난 문제라서 음수간선이 있어도, 그냥 다익스트라를 쓰면 되는줄 알았다. 
      문제를 접하고 Bellman-Ford 알고리즘에 대해서 알게되었고, 개념 먼저 공부하느라 뒷 문제들 보다 나중에 풀었다. 

    1. 음수 간선 순환 (Negative Cycle Graph)
    - Graph에 음수 간선이 포함된다고 해도 Dijkstra 알고리즘을 사용할 수 없는 것은 아니다. 
      음수 간선으로 인한 순환(Cycle)이 Graph에 생기지 않는다면, 여전히 Dijkstra를 사용해서 최단거리 문제를 해결할 수 있다. 

    - 하지만, Graph에 음수 간선이 포함되어 있고, 그 과정에서 Cycle이 생겨난다면, 최단거리가 음의 무한대로 발산하는 노드가 생기고
      이 노드를 거쳐가는 모든 노드 또한 최단거리가 음의 무한대로 발산하게 된다. 

    2. Bellman-Ford Algorithm
    - 따라서, 음수 간선이 포함된 Graph는 시간 복잡도의 손해를 보더라도(O(VE)) Bellman-Ford를 사용해서
      문제를 해결해야 음수 사이클이 생기는지를 알 수 있게 된다. 

    3. 이번 문제 풀이
    - 웜홀 문제는 Graph 내부에 음수 사이클이 생기는 경우만 판단하면 되는 문제이므로, 문제 내에서 start node에 대한 명시가 없다. 
      때문에 조금 헷갈렸고, dist[now] != INF 조건을 삭제하면서 해결할 수 있었다. 
      dist[now] != INF라는 말은 현재 노드를 통해서 거쳐 갈 수 있는 경우를 생각하려고 주는 조건인데, 
      싸이클이 생기는지 그렇지 않은지에 대해서만 판단하면 되므로, 어떤 특정 node에서 시작해서 현재 노드까지 오는 경우를 생각하지 않아도 되니까
      조건을 삭제해줌으로써, 문제를 해결할 수 있다. 

    - 위의 코드 12줄에서 edges에서 재밌는 점은 
      처음에는 edges[j][0], edges[j][1], edges[j][2] 이런식으로 값에 접근해서 사용했는데,
      다른 사람들이 제출한 코드에 비해서 1000ms 이상 손해를 보는 결과 값을 얻을 수 있었다. 

      자세히는 모르겠지만, in을 사용해서 하는 경우는 파이썬의 for loop 내부에서 리스트를 생성해서 접근하는 방식을 사용하는 것 같은데, 
      index을 하는 경우는 range함수만 사용해서 리스트에 접근하므로 3중 for문 처럼 사용됐다고 생각했다.       
"""