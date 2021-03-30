n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards_max = 0


# 카드 세 장을 뽑는다. 
for i in range(n-2): # 첫 번째 카드 
    for j in range(i+1, n-1): # 두 번째 카드
        for k in range(j+1, n): # 세 번째 카드 
            cards_sum = cards[i] + cards[j] + cards[k] # 카드 숫자합
            if cards_sum <= m and cards_sum > cards_max: # 조건 만족
                cards_max = cards_sum # 맥스 값 변환

print(cards_max)
