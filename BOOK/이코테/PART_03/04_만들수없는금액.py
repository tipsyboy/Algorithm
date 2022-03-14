n = int(input())
coins = list(map(int, input().split()))


target = 1  # 1원부터 target
for coin in coins:
    if coin > target:
        break
    target += coin

print(target)
