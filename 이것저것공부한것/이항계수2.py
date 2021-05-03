def bino_coef(n, k):
    if k > n:
        return 0

    cache = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    def choose(times, got):
        if times == n:
            return got == k

        if cache[times][got] != -1:
            return cache[times][got]

        cache[times][got] = choose(times + 1, got) + choose(times + 1, got + 1)
        # print(cache)
        return cache[times][got]

    return choose(0, 0)


print(bino_coef(100, 80))
