import sys
input = sys.stdin.readline


# graph가 같은 원소로 이루어져 있는지 check
def check_graph(x, y, length):
    flag = graph[x][y]

    for i in range(length):
        for j in range(length):
            if graph[x + i][y + j] != flag:
                return False

    return True


# quad_tree
def quad_tree(x, y, length):
    global rst

    # 1) 원소가 하나면 graph check 할 것 없이 값 추가하고 return
    if length == 1:
        rst += str(graph[x][y])
        return

    # 2) graph에 원소가 같지 않으면,
    if not check_graph(x, y, length):
        rst += "("  # 같지 않을때 괄호를 열고 닫으면서 각 구역을 구분함.
        for i in range(2):  # 4분할 한다.
            for j in range(2):
                # (x, y) = (row, col) 좌표 전달
                quad_tree(x + length//2*i, y + length//2*j, length//2)
        rst += ")"  # 닫기

        return

    rst += str(graph[x][y])  # 3) graph의 원소가 같으면 그냥 값을 추가해주면 된다.


n = int(input())
graph = [list(map(int, str(input().rstrip()))) for _ in range(n)]  # 중요
rst = ""

quad_tree(0, 0, n)
print(rst)
