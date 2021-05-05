def cut_board(x, y, length, number):
    if length == 2:
        if x == r and y == c:
            print(number)
        elif x == r and y + 1 == c:
            print(number + 1)
        elif x + 1 == r and y == c:
            print(number + 2)
        elif x + 1 == r and y + 1 == c:
            print(number + 3)
    else:
        # 찾아 들어가기
        half = length // 2
        if (x <= r < x + half) and (y <= c < y + half):  # 1
            cut_board(x, y, half, number)
        elif (x <= r < x + half) and (y + half <= c < y + length):  # 2
            cut_board(x, y + half, half, number + (half**2) * 1)
        elif (x + half <= r < x + length) and (y <= c < y + half):  # 3
            cut_board(x + half, y, half, number + (half**2) * 2)
        elif (x + half <= r < x + length) and (y + half <= c < y + length):  # 4
            cut_board(x + half, y + half, half, number + (half**2) * 3)


n, r, c = map(int, input().split())
cut_board(0, 0, 2**n, 0)
