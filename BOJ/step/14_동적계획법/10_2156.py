import sys


def drink_max_wine():
    n = int(sys.stdin.readline())
    wine = []

    for i in range(n):
        wine.append(int(sys.stdin.readline()))

    if n == 1:
        return wine[0]
    elif n == 2:
        return wine[0] + wine[1]

    wine_max = [0 for i in range(n)]
    wine_max[0] = wine[0]
    wine_max[1] = wine[0] + wine[1]
    wine_max[2] = max(wine_max[1], wine[0] + wine[2], wine[1] + wine[2])

    for i in range(3, n):
        # 1) 새 잔을 안마신다. X
        case1 = wine_max[i-1]  # 이전항과 같은 경우
        # 2) 새 잔을 마시고 바로 앞 잔을 안마신다. XO
        case2 = wine[i] + wine_max[i-2]
        # 3) 새 잔을 마시고 바로 앞 잔도 마신다. XOO
        case3 = wine[i] + wine[i-1] + wine_max[i-3]

        wine_max[i] = max(case1, case2, case3)

    return wine_max[n-1]


print(drink_max_wine())
