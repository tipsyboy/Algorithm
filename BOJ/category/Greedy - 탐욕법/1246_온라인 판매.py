import sys

input = sys.stdin.readline


N, M = map(int, input().split())
P = []
for _ in range(M):
    P.append(int(input()))
P.sort(reverse=True)

price, ans = 0, 0
for i in range(M):
    if (i + 1) > N:
        break

    if P[i] * (i + 1) >= ans:
        ans = P[i] * (i + 1)
        price = P[i]

print(price, ans)