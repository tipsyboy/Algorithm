# import time
import sys


def promising(level, now_col):
    for i in range(len(col_val)):
        if now_col == col_val[i] or abs(col_val[i] - now_col) == (level - i):
            return False

    return True


def n_queens(level):
    global count

    if level == n:
        count += 1
        # for i in range(n):
        #     print(f"({i}, {col_val[i]})")
        return

    for i in range(n):
        # 유망성 검사 - nonpromising 하면 건너 뛴다.
        if not promising(level, i):
            continue

        # promising 할 경우에
        col_val.append(i)  # 경로에 노드를 넣고
        n_queens(level + 1)  # 다음 행으로 이동한다.
        col_val.pop()  # 다시 돌아온 경우 -


n = int(sys.stdin.readline())  # n-Queens의 n, 레벨이됨
# start = time.time() # 코드 스타트
col_val = []
count = 0  # 되는거 개수 count

n_queens(0)
print(count)
# print(f"time: {time.time() - start}") # 알고리즘 돌아간 시간
