import sys

n = int(sys.stdin.readline())
fibo_lst = [0 for i in range(n+1)]  # fibonacci 저장할 리스트
fibo_lst[1] = 1

# 차례대로 구해나간다.
for i in range(2, n+1):
    fibo_lst[i] = fibo_lst[i-2] + fibo_lst[i-1]

print(fibo_lst[n])
