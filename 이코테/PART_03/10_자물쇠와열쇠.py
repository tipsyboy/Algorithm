def rotate_a_matrix_90_degree(matrix):
    row_len = len(matrix)  # 행 길이
    col_len = len(matrix[0])  # 열 길이

    rotated_matrix = [[0] * row_len for _ in range(col_len)]

    for i in range(row_len):
        for j in range(col_len):
            rotated_matrix[j][row_len - i - 1] = matrix[i][j]

    return rotated_matrix


def check_lock(new_lock):
    # 3배로 넓힌 new_lock의 중앙 검사하기 위해서
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False

    return True


def solution(key, lock):
    lock_len = len(lock)
    key_len = len(key)
    # 1. lock map을 key 검사가 편하게 넓힌다.
    new_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]

    # 2. 넓힌 new_lock map의 중앙에 원래 lock을 이식
    for i in range(lock_len):
        for j in range(lock_len):
            new_lock[i + lock_len][j + lock_len] = lock[i][j]

    # 3. key를 회전해가면서 map에 더해준다. (4방향)
    for rotation in range(4):
        key = rotate_a_matrix_90_degree(key)

        # 4. new_lock map을 돌면서
        for x in range(lock_len * 2):
            for y in range(lock_len * 2):

                # 4. key값을 new_lock에 더해주고
                for i in range(key_len):
                    for j in range(key_len):
                        new_lock[i + x][j + y] += key[i][j]
                # 4. 중앙의 lock을 풀었는지 check
                if check_lock(new_lock):  # 풀었으면 True를 리턴하고
                    return True

                # 6. 못 풀었으면 다시 key를 빼고 수행한다.
                for i in range(key_len):
                    for j in range(key_len):
                        new_lock[i + x][j + y] -= key[i][j]

    # 7. 모든 경우의 수를 다 해봤는데 안되면 False
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
