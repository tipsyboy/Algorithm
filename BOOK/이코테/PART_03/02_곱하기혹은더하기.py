seq = input()

result = int(seq[0])

for x in seq[1:]:
    if int(x) <= 1 or result <= 1:
        result += int(x)
    else:
        result *= int(x)


print(result)
