import sys

input = sys.stdin.readline


n, h = map(int, input().split())  # 동굴 길이(장애물 수), 동굴 높이

# 석순과 종유석의 크기별로 저장한다. idx 5의 값은 size가 5인 석순 또는 종유석의 개수
down = [0] * (h + 1)  # 석순
up = [0] * (h + 1)  # 종유석

for i in range(n):
    size = int(input())  # 석순 또는 종유석의 크기
    # 짝수 항에는 석순의 크기가 들어온다.
    if i % 2 == 0:
        down[size] += 1
    else:  # 홀수 항은 종유석
        up[size] += 1

# 뒤에서부터 석순과 종유석의 구간합을 구한다.
# ex) 크기 5의 석순은 5아래의 구간에서 모두 충돌하므로, 구간 합으로 개수를 찾는 것이 성립함.
# 따라서 이후에 idx1의 값은 각각(석순, 종유석)이 구간에서 부딪치는 횟수
# 다만 종유석의 경우 위에서 내려오는 형태이므로 이후에 처리가 필요
for i in range(h - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]


min_collision = n  # 최소 충돌 수
range_count = 0  # 최소 충돌 수의 개수

for i in range(1, h + 1):
    collison = down[i] + up[h - i + 1]
    if min_collision > collison:
        min_collision = collison  # 최소 충돌수 갱신
        range_count = 1  # 새로 센다.
    elif min_collision == collison:
        range_count += 1

print(min_collision, range_count)


"""
3020. 개똥벌레 (Gold 5)
    - 석순과 종유석의 크기별로 저장한다. idx 5의 값은 size가 5인 석순 또는 종유석의 개수
    
    - ex) 크기 5의 석순은 5아래의 구간에서 모두 충돌하므로, 구간 합으로 개수를 찾는 것이 성립함.
      따라서 이후에 idx1의 값은 각각(석순, 종유석)이 구간에서 부딪치는 횟수
      다만 종유석의 경우 위에서 내려오는 형태이므로 이후에 처리가 필요
"""
