def solution(prices):
    stack = []
    rst = [-1] * len(prices)

    for i in range(len(prices)):
        if not stack:
            stack.append((prices[i], i))
            continue

        while stack and stack[-1][0] > prices[i]:
            price, idx = stack.pop()
            rst[idx] = i - idx
        stack.append((prices[i], i))

    while stack:
        price, idx = stack.pop()
        rst[idx] = len(prices) - 1 - idx

    return rst

prices = [1, 2, 3, 2, 3]
solution(prices)