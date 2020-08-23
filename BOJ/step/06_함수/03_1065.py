import sys


def num_of_hansu(num):
    # 한 자리수, 두 자리수는 모두 한수이다.
    if num < 100:
        return num

    hansu = 99
    for i in range(100, num + 1):
        check = str(i)
        d = int(check[1]) - int(check[0])  # 공차
        flag = False

        for j in range(1, len(check)-1):
            if (int(check[j+1]) - int(check[j])) != d:
                flag = True
                break

        if flag == False:
            hansu += 1

    return hansu


N = int(sys.stdin.readline())

print(num_of_hansu(N))
