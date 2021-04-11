input_str = input()
result = []
sum_value = 0

for s in input_str:
    if s.isalpha():
        result.append(s)
    else:
        sum_value += int(s)

result.sort()

if sum_value:
    result.append(str(sum_value))

print("".join(result))
