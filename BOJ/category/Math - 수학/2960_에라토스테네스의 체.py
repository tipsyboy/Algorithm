import sys

input = sys.stdin.readline

N, K = map(int, input().split())
sieve = [False, False] + [True] * (N - 1)
cnt = 0
for i in range(2, N + 1):
    if not sieve[i]:
        continue
    flag = False
    for j in range(i, N + 1, i):
        if not sieve[j]:
            continue
        sieve[j] = False
        cnt += 1
        if cnt == K:
            print(j)
            flag = True
            break

    if flag:
        break
