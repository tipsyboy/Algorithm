import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 동전 종류 수, target 금액
coins = []
rst = 0

# coin 입력
for _ in range(n):
    coin = int(input())

    # 타겟 금액보다 크면 어차피 사용할 수 없으니 list에 추가하지 않음
    if coin < k:
        coins.append(coin)

coins.reverse()  # 오름차순으로 입력 받으므로 계산 편하게 reverse

# 나눠 줌
for coin in coins:
    if k >= coin:
        rst += k // coin
        k %= coin

print(rst)


"""
    전형적인 greedy 알고리즘 문제 
"""
