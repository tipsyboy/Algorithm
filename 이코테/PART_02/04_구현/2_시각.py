n = int(input())

count = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s):
                count += 1

print(count)

# 완전탐색
# 하루는 86400s 밖에 되지 않으므로 전부 다 검색해서 찾아본다.
# 완전탐색은 데이터의 개수가 100만개 아래일 때,
# -> 100만개 이상의 데이터를 다루는 경우 완전탐색의 경우가 아닐 가능성이 높다.
