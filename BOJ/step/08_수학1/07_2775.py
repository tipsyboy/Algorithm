import sys

T = int(sys.stdin.readline())


for i in range(T):
    k = int(sys.stdin.readline())  # 층 수
    n = int(sys.stdin.readline())  # 호 수

    x = [j for j in range(1, n+1)]

    for a in range(k):
        for b in range(1, n):
            x[b] += x[b-1]

    print(x[n-1])
