

# 1. 틀린 답 - 반례
def solution(n, lost, reserve):
    for stu in reserve:
        if stu in lost:
            lost.remove(stu)
        elif stu-1 in lost:
            lost.remove(stu-1)
        elif stu+1 in lost:
            lost.remove(stu+1)

    ans = n - len(lost)

    return ans
    """
    이 코드를 사용하면 
    [체육복을 도난당하고 + 여분을 가져온 학생]의 앞 학생이 
    [도난x + 여분o]인 경우 앞에놈이 체육복을 빌려줌.
    이 경우에 더 많은 학생이 체육복을 입는 결과를 만들 수 있지만, 
    여분을 가져온 놈이 남의 옷을 입는다 (조건 위배)
    따라서 solution_2의 경우처럼 [도난o + 여분o]의 경우를 먼저 전처리한다. 
    """


def solution_2(n, lost, reserve):
    # [도난o + 여분o]의 경우를 먼저 전처리
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost)-set(reserve)

    for stu in reserve_set:
        if stu-1 in lost_set:
            lost_set.remove(stu-1)
        elif stu+1 in lost_set:
            lost_set.remove(stu+1)

    return n - len(lost_set)


# print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(5, [2, 4], [3]))
# print(solution(3, [3], [1]))
# 반례
print(f"sol1: {solution(5, [3, 4, 5], [2, 3, 4])}")
print(f"sol2: {solution_2(5, [3, 4, 5], [2, 3, 4])}")
