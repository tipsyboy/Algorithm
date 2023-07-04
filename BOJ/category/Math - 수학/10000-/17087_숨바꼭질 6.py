# https://www.acmicpc.net/problem/17087

"""
17087. 숨바꼭질 6
    1. 수빈이는 위치 X에서 X+D, X-D 로 이동할 수 있다. 
    2. 때문에 수빈이의 시작점 S에서 D씩 앞뒤로 이동해서 모든 동생의 위치로 갈 수 있어야 한다. 
    3. D의 최댓값을 구해야 하므로 최대공약수를 활용해서 찾는다.
"""


import sys

input = sys.stdin.readline


def gcd(x: int, y: int) -> int:
    while y:
        r = x % y
        x = y
        y = r

    return x


def sol(N: int, S: int, diff: list) -> int:
    if N == 1:
        return diff[0]

    ans = gcd(diff[0], diff[1])
    for i in range(2, N):
        ans = gcd(ans, diff[i])

    return ans


N, S = map(int, input().split())
A = list(map(int, input().split()))

diff = []
for e in A:
    diff.append(abs(S - e))

print(sol(N, S, diff))