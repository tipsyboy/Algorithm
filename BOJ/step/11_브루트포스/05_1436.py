
# 1) 처음부터 다 찾는다.
num = int(input())
num_666 = 666
count = 1

while num > count:
    num_666 += 1
    if "666" in str(num_666):
        count += 1

print(num_666)


# 더 좋은 방법이있을까
