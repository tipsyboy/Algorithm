# DP 1 (Dynamic Programming 1)
import sys

test_case = int(sys.stdin.readline())
fibo_lst = [0 for i in range(41)]
fibo_lst[1] = 1

for i in range(test_case):
    n = int(sys.stdin.readline())

    # n이 0인 경우.
    if n == 0:
        print(1, 0)
        continue

    if fibo_lst[n]:  # 미리 구해놔서 리스트에 존재하면
        print(fibo_lst[n-1], fibo_lst[n])
    else:  # 존재 안하면 새로 구함
        for j in range(2, n+1):
            fibo_lst[j] = fibo_lst[j-2] + fibo_lst[j-1]

        print(fibo_lst[n-1], fibo_lst[n])
