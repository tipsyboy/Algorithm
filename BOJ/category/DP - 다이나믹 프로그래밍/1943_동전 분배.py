import sys

input = sys.stdin.readline


def solution(coins: dict) -> bool:
    total = 0
    for coin, cnt in coins.items():
        total += coin * cnt

    # 1. 총 금액을 정확히 둘로 나눌 수 없으면 이미 안됨
    if total % 2 != 0:
        return False

    # dp[i] = i원을 만들 수 있는가 ?
    dp = [False] * (total // 2 + 1)
    dp[0] = True  # 당연히 0원은 만들 수 있다.

    for coin in coins:
        if coin > total // 2:  # 2.
            return False

        for target in range(total // 2, coin - 1, -1):  # 3.
            if not dp[target - coin]:  # 4.
                continue

            # 5.
            for num in range(coins[coin]):
                if target + coin * num > total // 2:
                    break
                dp[target + coin * num] = True

            if dp[total // 2]:
                return dp[total // 2]

    return dp[total // 2]


for _ in range(3):
    N = int(input())
    coins = dict()
    for __ in range(N):
        coin, cnt = map(int, input().split())
        coins[coin] = cnt

    print(1) if solution(coins) else print(0)


"""
1943. 동전 분배
    - 0. dp[i]의 정의 => i원을 만들 수 있는가 ?

    - 1. 총 금액을 둘로 나누는 문제, 따라서 나눌 수 없으면 False
    - 2. coin의 단위가 total의 절반보다 크면 당연히 False
    
    - 3. 이 문제에서 가장 중요한 포인트
      왜 큰 돈의 단위부터 탑다운으로 내려가면서 판단하는가?
      -> 이전에 쓰인 코인이 재활용 되는 경우 따위를 방지하기 위해서
      예를 들어 뒤에서 동전의 개수만큼 True로 변환하는 과정이 있는데,
      이때 2원이 true라면 이 돈이 1원 2개인지, 2원 1개인지 모르고 이러한 점이 앞의 경우에서 코인이 재활용되는 경우임.

    - 4. 이전에 만들 수 없는 금액이었으면 현재 코인을 추가해도 만들 수가 없다. 
    - 5. target money에서 코인의 개수를 고려해 만들 수 있는 금액을 갱신한다. 
"""