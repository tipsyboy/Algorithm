import sys
input = sys.stdin.readline


def backtracking(depth):
    if depth == m:
        if tuple(rst) not in visited_set:
            print(" ".join(map(str, rst)))
            visited_set.add(tuple(rst))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            rst.append(numbers[i])
            backtracking(depth + 1)
            visited[i] = False
            rst.pop()


def backtracking2(depth):
    if depth == m:
        print(" ".join(map(str, rst)))
        return

    # 현재 depth에서 이전 숫자를 검사 numbers가 소팅된 상태이므로 이전 숫자들이랑 겹치지만 않으면 됨
    before = -1
    for i in range(n):
        if not visited[i] and numbers[i] != before:
            rst.append(numbers[i])
            visited[i] = True
            before = numbers[i]
            backtracking2(depth + 1)
            visited[i] = False
            rst.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
visited = [False] * n
rst = []
# visited_set = set()

# # 1)
# backtracking(0)
backtracking2(0)

"""
07. 15663 N과 M (9) (Silver 2)
    - 첫 번째 시도 방법
      기존의 N과 M의 방식을 그대로 사용하면서 visited_set 자료구조를 하나 더 선언했다.
      depth가 m까지 도달해서 출력하려고 할때 rst list를 tuple로 캐스팅해서 visited_set을 검사하고
      해당 수열이 존재하면 출력하지 않고 그대로 리턴한다. 존재 하지 않으면 출력하고 visited_set에 추가해준다. 

      visited_set은 set() 자료구조로 선언해서 탐색에서 O(1)의 시간복잡도를 갖게해서 시간초과를 피했다. 
      하지만 탐색 과정에서 미리 찾아내는 것이 아니라 출력 직전에 검사하는 것이기 때문에
      두 번째 방법 보다는 손해가 있다. 

    - 두 번째 방법
      함수 내부에서 before 변수를 하나 두고, 이전 숫자와 같은 경우에는 스킵하는 방법이다. 
      numbers가 소팅되어 있는 상태기 때문에 이전 숫자와 같은 경우만 출력하지 않으면 된다. 
      같은 위치의 숫자는 당연히 visited로 검사를 하고 같은 depth에서 같은 숫자는 before 변수로 검출한다. 

      before 변수를 통해서 재귀를 돌지 않고 미리 안되는 숫자를 검사하기 때문에 위의 방식보다는
      속도 측면에서 이득을 가져올 수 있는 방법이다. 
"""
