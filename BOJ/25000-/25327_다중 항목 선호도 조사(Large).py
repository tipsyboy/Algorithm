import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
table = dict()
for _ in range(n):
    fav = input().split()

    for i in range(4):
        for combi in combinations(fav, i):
            key = "".join(combi)
            table[key] = table.get(key, 0) + 1

for _ in range(m):
    query = "".join(input().replace("-", "").split())
    if query not in table:
        print(0)
        continue
    print(table[query])


"""
25327. 다중 항목 선호도 조사(Large)
    - 카카오 2021 순위검색? 그 문제에서 아이디어 얻어서 해결함

    - 학생의 선호도를 파싱해서 3가지에서 가질 수 있는 모든 항목을 키 값으로 갖는 딕셔너리를 만들고 찾아나간다. 
      sum(3Ci) [i <- 0..3]을 하면 8가지씩 경우를 가질 수 있고,
      딕셔너리의 총 key값이 64가지로 저장할 수 있다.

    - 이제 각각의 쿼리에 대해서 파싱 후 저장한 값을 불러내오기만 하면 끝

    - 카카오 2021에서 비슷한 문제는 최종 쿼리 처리에서 이진탐색을 통해서 값을 다시 찾는 과정이 있었으나
      이 문제에서는 그런건 없었다.
"""