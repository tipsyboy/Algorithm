import sys
input = sys.stdin.readline


def promising(row):

    for i in range(row):
        # if col[row] == col[i]: # 열 검사인데 visited를 통해서 삭제한다.
        #     return False

        # 대각선만 검사
        if abs(col[row] - col[i]) == row - i:
            return False

    return True


def n_queens(row):
    global rst

    if row == n:
        rst += 1
        return

    for i in range(n):
        col[row] = i

        # 같은 열에 있는지 검사
        if visited[i]:
            continue

        if promising(row):
            visited[i] = True  # 놓고
            n_queens(row + 1)
            visited[i] = False  # 돌아오면 뺌


n = int(input())
rst = 0
col = [0] * n
visited = [False] * n  # 열 방문 검사
n_queens(0)
print(rst)


"""
22. 9663 N-Queen (Gold 5)
    1. 
    - 백트래킹 문제로 유명한 N-Queen 문제이다. 
      사실 이전에 풀어봤었는데, 그때 어떻게 공부를 했던건지 계속 틀렸다. 

    - 문제를 풀다보면 계속된 시간초과에 부딪히는데, 나름 정해 라고 풀리는 모든 방법이 boj python3에서는 모두 TLE 판정을 받는다......
      백트래킹 문제는 python3으로는 매우 느리지 사용하지 않는것이 정해라고 할 정도였다. 

    - 같은 열 promising까지 visited[] 리스트로 분리해서 처리해줬을때, pypy3로 겨우 통과 할 수 있었다. 

    2. 문제 해설
    - 체스판에서 만약 (0, 0)에 퀸을 놓는 경우에 앞으로 0행에는 모두 퀸을 놓을 수 없다. (당연하다.)
      따라서 행(row)을 기준으로 현재 행에 퀸을 놓는 경우 row+1 재귀호출을 통해서 다음 행으로 넘어간다. 
      
      이제, 같은 열과 대각선에 위치하는 경우를 따져야 하는데, 원래 코드에서는 promising() 함수에서 한꺼번에 처리해 줬다. 
      col[] 리스트를 하나 선언해두고, 현재 퀸을 놓아야 하는 위치까지 퀸이 놓아져 있었다면(col[row] == col[i]) False를 리턴한다. 

      대각선의 경우에는 현재 퀸을 놓은 자리에서 행/열이 같은 숫자로 이동을 하는 경우이므로 행끼리 열끼리 차가 같은 경우에 
      대각선에 위치한다고 생각할 수 있다. 이때, 대각선의 방향은 사방으로 다 있으므로 절댓값을 사용해서 계산한다. 
      (promising()의 row - i의 경우는 i가 row 까지만 돌고 있으므로 절댓값을 해줄 필요가 없다.)
      
      이제 이렇게 되면 모든 행/열/대각선을 검사하게 되는 것이 되고 n개의 퀸을 놓을수 있는 위치를 찾을 수 있다. 

      하지만, promising()에서 열/대각선을 모두 검사하는 경우 pypy3에서도 TLE를 받게된다... (행은 이미 구분되어 있음)
      따라서 promising() 진입 전에(promising()의 for loop를 돌기 전에) visited[]를 통해서 체스판의 열값의 중복 여부를 찾는다.
      (n과 m에서 했던 방식)
      
      pypy3로 겨우 AC 받았다.
"""
