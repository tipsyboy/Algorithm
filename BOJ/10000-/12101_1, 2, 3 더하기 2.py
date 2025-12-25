# 2024.06.14 FRI
# https://www.acmicpc.net/problem/12101

import sys

input = sys.stdin.readline


# sol 1
def build_nth_exp(cur):
    if cur in dp:
        return dp[cur]

    rst = []
    for i in range(1, 4):
        for exp in build_nth_exp(cur - i):
            rst.append(exp + "+" + str(i))

    dp[cur] = rst
    return dp[cur]


# sol 2
def find_kth_exp(cur, exp):
    global ans, k

    if cur == 0:
        k -= 1
        if k == 0:
            ans = "+".join(map(str, exp))
        return

    for i in range(1, 4):
        if cur - i >= 0:
            exp.append(i)
            find_kth_exp(cur - i, exp)
            exp.pop()


n, k = map(int, input().split())

# sol 1
dp = {1: ["1"], 2: ["1+1", "2"], 3: ["1+1+1", "1+2", "2+1", "3"]}

build_nth_exp(n)
dp[n].sort()
print(-1) if len(dp[n]) < k else print(dp[n][k - 1])

# sol 2
ans = -1
find_kth_exp(n, [])
print(ans)
