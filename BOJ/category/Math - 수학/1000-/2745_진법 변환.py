import sys

input = sys.stdin.readline

N, B = input().split()

base = int(B)
ans = 0
for i in range(len(N) - 1, -1, -1):
    if N[i].isalpha():
        ans += (base ** (len(N) - 1 - i)) * (ord(N[i]) - 55)
    else:
        ans += (base ** (len(N) - 1 - i)) * int(N[i])

print(ans)
