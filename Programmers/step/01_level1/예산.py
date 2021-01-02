def divide_budget(dept, budget):
    dept.sort()
    cnt = 0

    for d in dept:
        budget -= d

        if budget < 0:
            break

        cnt += 1

    return cnt


print(divide_budget([1, 3, 2, 5, 4], 9))
print(divide_budget([2, 2, 3, 3], 10))
