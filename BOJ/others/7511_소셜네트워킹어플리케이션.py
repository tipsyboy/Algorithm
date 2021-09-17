import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10**6) # 메모리초과;;?


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution():
    tc = int(input())

    for i in range(tc):
        n = int(input())  # user 수 (0 ~ n-1)

        # init parent table
        parent = [0] * n
        for j in range(n):
            parent[j] = j

        k = int(input())  # 친구 관계수 - 연결관계
        for _ in range(k):
            a, b = map(int, input().split())

            union_parent(parent, a, b)

        query = int(input())  # 쿼리
        print("Scenario %d:" % (i + 1))
        for _ in range(query):
            a, b = map(int, input().split())

            if find_parent(parent, a) == find_parent(parent, b):  # 친구 관계일때,
                print(1)
            else:  # 아닐때
                print(0)

        print()


solution()


"""
7511. 소셜 네트워킹 어플리케이션 (Gold 5)
    - 문제 자체는 별로 어려울것 없는 유니온-파인드인데, pypy3로 제출했을때, MLE가 난다. 
    
    - 유저 수가 많아서 find 도중 재귀호출 수가 많아질줄 알고 재귀범위를 늘려줬는데, 그 부분에서 MLE가 났던것 같다.. 

      자세한 내용은 모르겠지만 4번줄을 제거해줬더니 AC받았다. 나중에 찾아보도록
"""
