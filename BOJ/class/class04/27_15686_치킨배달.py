import sys
from itertools import combinations
input = sys.stdin.readline
INF = int(1e9)


def get_chicken_dist(case):
    chicken_dist = 0

    for house in houses:
        x, y = house
        dist = INF
        for ch in case:
            dist = min(dist, abs(x - ch[0]) + abs(y - ch[1]))

        chicken_dist += dist

    return chicken_dist


n, m = map(int, input().split())
graph = []
houses = []
chicken = []
rst = INF

for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        if temp[j] == 1:
            houses.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))

for case in combinations(chicken, m):
    rst = min(rst, get_chicken_dist(case))

print(rst)


"""
27. 15686 치킨 배달 (Gold 5)
    - 간단한 구현문제 + 조합이다. 

    - 문제에서 m개의 치킨집만 남긴다고 했으므로 처음 graph를 입력 받을 때, 모든 치킨집의 좌표를 저장해 준뒤에
      combinations를 통해서 m개의 치킨집만 선택한다. (이전문제 연구소와 같은 방법으로)
      또한, 이 문제에서는 graph를 직접 저장할 필요도 없다. 

      이후에 모든 집에서 조합된 m개의 치킨집중에 최솟값을 치킨 거리만 채택해서 결과 값에 저장해주어 리턴하면 된다. 

    - 마지막으로 위의 리턴 값을 가지고 전체의 결과 값과의 비교를 해주면 된다. 

    - 어렵지 않은 문제였으나, 골드5의 난이도를 갖고 있는데, 아마 combinations을 사용하지 않은 구현 방법에서
      어려운 부분이 있을 것 같다 (아마 백트래킹이겠지)
      
      다른 방법으로 다시 구현해볼 필요가 있을것 같다. 
"""
