def solution(numbers, hand):
    major_hand = hand[0].upper()
    keypad = [[1, 4, 7, "*"], [2, 5, 8, 0], [3, 6, 9, "#"]]
    left_hand = [0, 3]  # 시작점 *, #의 좌표
    right_hand = [2, 3]
    rst = []

    for num in numbers:
        if num in keypad[0]:
            left_hand = [0, keypad[0].index(num)]
            rst.append("L")
        elif num in keypad[2]:
            right_hand = [2, keypad[2].index(num)]
            rst.append("R")
        elif num in keypad[1]:
            l_dist = abs(left_hand[0] - 1) + abs(left_hand[1] - keypad[1].index(num))
            r_dist = abs(right_hand[0] - 1) + abs(right_hand[1] - keypad[1].index(num))

            if l_dist == r_dist:
                if major_hand == "R":
                    right_hand = [1, keypad[1].index(num)]
                    rst.append(major_hand)
                else:
                    left_hand = [1, keypad[1].index(num)]
                    rst.append(major_hand)
            elif r_dist > l_dist:
                left_hand = [1, keypad[1].index(num)]
                rst.append("L")
            else:
                right_hand = [1, keypad[1].index(num)]
                rst.append("R")

    return "".join(rst)


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
