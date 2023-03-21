# https://www.acmicpc.net/problem/1790

import sys

input = sys.stdin.readline


def sol(N: int, k: int) -> int:
    d, nine = 1, 9
    sumv = 0
    while sumv + d * nine < k:
        sumv += d * nine
        d += 1
        nine *= 10

    start = 10 ** (d - 1)  #
    q, r = (k - sumv - 1) // d, (k - sumv - 1) % d  # (k - sumv - 1)에 대해

    if start + q > N:
        return -1

    return int(str(start + q)[r])


N, k = map(int, input().split())
print(sol(N, k))


"""
1790. 수 이어  쓰기 2
    - 생각한 난이도에 비해서 계산이 계속 삑사리나서 좀 오래 걸렸음

    1. k번째 수의 자릿수 d를 먼저 구하고
    2. target이 d자릿수의 x번째 수임을 구한다.
    3. str로 바꿔주고 최종적으로 k번째 수를 구하면 끝

    내 코드에서 start가 d자리의 첫 번째 숫자를 의미하는데 이때 아무 생각 없이 (k - sumv)//d 를 더해주면 
    첫 번째 숫자를 무시하고 두 번째 숫자부터 한 칸씩 나아가게 된다. 
    따라서 (k - sumv - 1)를 갭으로 두고 d자리 수에 맞게 계산해서 풀이해주어 AC를 받을 수 있었다.
"""