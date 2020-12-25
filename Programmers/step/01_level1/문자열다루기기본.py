def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True

    return False


def solution2(s):
    return len(s) in (4, 6) and s.isdigit()


print(solution2("a234"))
print(solution2("1234"))
