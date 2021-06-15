import sys
input = sys.stdin.readline


def backtracking(idx, depth):
    if depth == m:
        print(" ".join(map(str, rst)))
        return

    before = -1
    for i in range(idx, n):
        if numbers[i] != before:
            rst.append(numbers[i])
            before = numbers[i]
            backtracking(i, depth + 1)
            rst.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
rst = []
backtracking(0, 0)


"""
07. 15663 N과 M (12) (Silver 2)
    - 15663 N과 M (9)와 같은 문제로 비내림차순 출력을 원하고 있기 때문에 idx를 추가해서 
      탐색 범위를 제한 해준다. 

    - 15663 N과 M (9)에서 풀었던 것처럼 당연히 튜플을 사용하는 방법광
      before로 이전 출력 원소 값을 저장하는 방법이 두개 존재한다. 

    - idx / i를 함수호출 할 때 인수를 주의하자
"""
