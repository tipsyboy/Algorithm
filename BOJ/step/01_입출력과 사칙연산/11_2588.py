a = int(input())
b = int(input())

rst1 = a * (b % 10)  # b 를 10으로 나눈 나머지
rst2 = a * ((b % 100) // 10)  # b를 100으로 나눈 나머지의 10으로 나눈 몫
rst3 = a * (b // 100)  # b 를 100으로 나눈 몫

print(rst1)
print(rst2)
print(rst3)
print(a*b)
