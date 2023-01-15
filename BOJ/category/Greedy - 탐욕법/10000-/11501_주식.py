import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N = int(input())
    stock_price = list(map(int, input().split()))

    max_price = stock_price[N - 1]
    ans = 0
    for i in range(N - 2, -1, -1):
        if max_price < stock_price[i]:
            max_price = stock_price[i]
            continue

        ans += max_price - stock_price[i]

    print(ans)

"""
11501. 주식
    - 가격을 뒤에서부터 훑으면서 i번째 값이 이전의 값보다 적은 경우 팔아치움
"""