import sys

input = sys.stdin.readline

lo, hi = map(int, input().split())

sieve = [1] * (hi - lo + 1)
num = 2
while num * num <= hi:
    square = num * num

    if (lo // square) * square < lo:
        start = (lo // square + 1) * square
    else:
        start = (lo // square) * square

    for i in range(start, hi + 1, square):
        sieve[i - lo] = 0

    num += 1

print(sum(sieve))


"""
1016. 제곱 ㄴㄴ수 
    - 범위 내의 1보다 큰 제곱수로 나누어 떨어지지 않는 수(제곱 ㄴㄴ수)의 개수를 찾는 문제
    - 거꾸로 제곱수를 곱해 나가면서 나오는 수들을 제거해주면 된다. 

    - 에라토스테네스의 체를 응용
    - 제곱수의 시작 범위를 어떻게 정할 것인가?
    - 큰 수의 체에서 범위를 어떻게 정하고 어떻게 저장할 것인가?

    - 문제에서 min의 범위가 1조로 매우 크지만 max와의 차이가 10^6 백만으로 체를 사용할 충분한 범위가 된다. 
      따라서 sieve에 저장할 때, -min값을 해주면서 저장한다. 
    - 또, min보다 크거나 같고 max보다 작거나 같은 수를 start로 설정해야 하기 때문에 전처리가 약간 필요하다. 
"""