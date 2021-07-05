import sys
input = sys.stdin.readline


# 1. combination의 정의를 이용한 방법
def combi(n, r):
    def factorial(n):
        rst = 1

        for i in range(1, n + 1):
            rst *= i

        return rst

    return factorial(n) // factorial(n - r) // factorial(r)


# 2. 이항계수의 성질 이용
def bino_coef(n, r):
    # 1) 이항계수 성질 이용 -> nCr = nCn-r
    r = (n - r) if n - r < r else r

    # 1) 파스칼 삼각형 초기화 -> 필요 부분까지만 만듬
    cache = [[0] * (r + 1) for _ in range(n + 1)]

    # 2) 성질 이용한 파스칼 삼각형 초기값 -> nC0 = 1 / nCn = 1
    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(r + 1):
        cache[i][i] = 1

    # 3) 성질 이용해서 계산 -> nCr = n-1Cr + n-1Cr-1
    for i in range(1, n + 1):
        for j in range(1, r + 1):
            cache[i][j] = cache[i-1][j-1] + cache[i-1][j]

    return cache[n][r]


# 3. 직접 뽑는 행위 - 확장성이 좋다.
def bino_coef2(n, r):
    if n < r:
        return 0

    cache = [[-1] * (n+1) for _ in range(n + 1)]

    def choose(times, got):
        if times == n:
            return got == r

        if cache[times][got] != -1:
            return cache[times][got]

        cache[times][got] = choose(times + 1, got) + choose(times + 1, got + 1)

        return cache[times][got]

    return choose(0, 0)


n, m = map(int, input().split())
# print(combi(n, m))
# print(bino_coef(n, m))
print(bino_coef2(n, m))


"""
12. 2407 조합 (Silver 2)
    - 조합의 정의를 물어보는 문제였던것 같다. factorial을 이용한 조합식의 정의대로 계산하면 
      문제에서 범위가 크지 않기 때문에 널널하게 통과할 수 있다. 
    
    - itertools의 combinations을 import해서 계산 후에 len()으로 수를 세면 어떨까 생각해 봤는데,
      그렇게는 안되더라... 리턴 값이 combinations obj인 것도 있고, 리스트로 변환시켜서 len()을 써도 값이 제대로 안나온다. 

    - 첫 번째 방법은 그냥 combination의 정의로 통과했고, 이후에 예전에 공부했던 이항계수의 성질을 복습할겸
      두 번째 방법으로 풀어보았다. 
      하는김에 속도 차이도 확인해봤는데 거의 100000수가 넘어가야 dp를 활용하는 방법이 더 빠르게 작동하기 시작한다.
    
    - 2번째 방법은 블로그 검색을 통해서 코드를 공부했는데, 조합의 성질을 이용해서 더 작은 수를 계산하면 빨라지더라. 

    - 3번째 방법도 블로그 검색을 통했는데, 재밌는 방법이었다. 
      
"""
