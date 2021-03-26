while True:
    numbers = list(map(int, input().split()))

    if sum(numbers) == 0:
        break

    hyp = max(numbers)
    numbers.remove(hyp)

    if hyp**2 == numbers[0]**2 + numbers[1]**2:
        print("right")
    else:
        print("wrong")
