n = int(input())

i = 1
while True:
    if n - i * 6 > 0:
        n -= i*6
        i += 1
    else:
        break

if n == 1:
    print(i)
else:
    print(i+1)
