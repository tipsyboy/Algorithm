# # 1)
# import sys

# input = sys.stdin.readline


# n = int(input())

# while n > 1:
#     for i in range(2, n + 1):
#         if n % i == 0:
#             print(i)
#             n //= i
#             break


# 2)
import sys

input = sys.stdin.readline


def eratos(n):
    n = int(n ** 0.5) + 1
    sieve = [False, False] + [True] * (n - 1)
    prime_numbers = []

    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i + i, n + 1, i):
            sieve[j] = False

    for i in range(2, n + 1):
        if sieve[i]:
            prime_numbers.append(i)

    return prime_numbers


n = int(input())
prime_numbers = eratos(n)
idx = 0
print(prime_numbers)
if n > 1:
    while idx < len(prime_numbers):
        while n % prime_numbers[idx] == 0:
            print(prime_numbers[idx])
            n //= prime_numbers[idx]

        idx += 1

if n != 1:
    print(n)


"""
11653. 소인수분해 (Silver 4)
    1.
    - 1) 깊게 생각할 필요 없이 2부터 시작해서 n을 계속 나누어 떨궈주면 된다. 
    - 2) 1)의 정당성은 소수는 수의 구성 최소 단위로 사용되므로, 
         합성수로 나누어지기 이전에 먼저 소수로 나누어 떨어져 for문을 탈출하기 때문이다.
    
    2.
    - 1) 미지수 x의 소인수를 구하려면 x의 약수인 소수들을 찾아야한다. 
      
      ex) x = 80 = (2^4 * 5)일때, 약수 = [1, 2, 4, 5, 8, 10, 16, 20, 40, 80], 약수중 소수 = [2, 5]
    
    - 2) 때문에 미지수 x 이하의 소수를 찾아야 하는데, 이때 에라토스테네스의 체를 이용해서 찾아준다. 
      ex) x = 80, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
    
    - 3) 하지만 10^7의 범위에서 O(√n)을 해도 1s 안에서는 TLE를 받는다.

    - 4) 그런데 여기서 x의 인수가  √x를 넘어서면, 그 인수는 1개밖에 사용할 수 없음.
      왜냐하면, 당연히 (√x)^2의 값이 x이므로, √x까지가 2개 인수 사용의 마지노선이다.

    - 5) 따라서, 우선 √x까지의 소수만 전부 구한 후, 이 범위 안에서 x의 소인수를 전부 찾아준다.
      그때, 남은 n의 값이 1이 아니라면, 그 자체가 1개만 사용할 수 있는 마지막 소인수가 되는 것이다.
      (왜냐하면, n이 소인수가 아닌 합성수일 경우 앞서 구한 √x의 소인수에 의해 이미 분해 됐을 것이다.)   
"""