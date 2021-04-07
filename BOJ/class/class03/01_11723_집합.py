import sys
input = sys.stdin.readline

m = int(input())

bit_set = 0
# 가지는 정수 x의 범위는 (1 <= x <= 20)
for _ in range(m):
    command = input().split()

    if command[0] == "all":
        bit_set = (1 << 21) - 1
    elif command[0] == "empty":
        bit_set = 0
    else:
        number = int(command[1])  # 두 번째 인자

        if command[0] == "add":
            bit_set |= (1 << number)
        elif command[0] == "remove":
            bit_set &= ~(1 << number)
        elif command[0] == "check":
            if (bit_set & (1 << number)) == 0:
                print(0)
            else:
                print(1)
        elif command[0] == "toggle":
            bit_set ^= (1 << number)
