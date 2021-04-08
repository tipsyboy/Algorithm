d = [0] * 100


# 재귀 fibo(탑 다운)
def fibo(x):
    print(f"({str(x)})", end=" ")
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)

    return d[x]


# 반복 fibo(바텀 업)
def fibo_2(x):
    d[1] = 1
    d[2] = 1

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[x]


print(fibo_2(6))
