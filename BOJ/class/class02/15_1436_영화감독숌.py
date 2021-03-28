n = int(input())

series = [666]
count = 1666
while True:
    if n == len(series):
        break

    if "666" in str(count):
        series.append(count)

    count += 1

print(series[-1])
