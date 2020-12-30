def solution_1(board, moves):
    height = len(board)
    answer = 0

    bucket = []

    for move in moves:
        temp = -1
        for i in range(height):
            if board[i][move - 1] != 0:
                temp = board[i][move - 1]
                board[i][move - 1] = 0
                break

        if temp == -1:
            continue

        if not bucket:
            bucket.append(temp)
        else:
            if bucket[-1] == temp:
                bucket.pop()
                answer += 2
            else:
                bucket.append(temp)

    # print(bucket)
    return answer


def solution_2(board, moves):
    height = len(board)
    answer = 0
    bucket = []

    for move in moves:
        for i in range(height):
            if board[i][move - 1] != 0:
                bucket.append(board[i][move - 1])
                board[i][move - 1] = 0

                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop()
                        bucket.pop()
                        answer += 2

                break

    return answer


b = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
m = [1, 5, 3, 5, 1, 2, 1, 4]

# a = solution_1(b, m)
a = solution_2(b, m)

print(a)
