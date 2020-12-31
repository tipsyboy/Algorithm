def isHarshad(x):
    digit_sum = 0
    num = str(x)

    for i in range(len(num)):
        digit_sum += int(num[i])

    if x % digit_sum == 0:
        return True
    else:
        return False


def isHarshad2(x):
    digit_sum = sum([int(num) for num in str(x)])
    print(digit_sum)


print(isHarshad2(10))
print(isHarshad2(12))
print(isHarshad2(11))
print(isHarshad2(13))
