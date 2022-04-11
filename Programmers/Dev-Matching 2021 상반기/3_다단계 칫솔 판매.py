def solution(enroll, referral, seller, amount) -> list:
    parent = dict()
    profit = dict()

    for en, ref in zip(enroll, referral):
        parent[en] = ref
        profit[en] = 0

    for s, a in zip(seller, amount):
        money = a * 100
        now_seller = s
        while True:
            if int(money * 0.1) < 1:
                profit[now_seller] += money
                break

            profit[now_seller] += money - int(money * 0.1)
            money = int(money * 0.1)
            now_seller = parent[now_seller]

            if now_seller == "-":
                break

    return list(profit.values())


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
solution(enroll, referral, seller, amount)

"""
"""