def solution(seoul):
    idx = seoul.index("Kim")
    answer = f"김서방은 {idx}에 있다"

    return answer


def solution2(seoul):
    for idx, name in enumerate(seoul):
        if name == "Kim":
            return f"김서방은 {idx}에 있다"


print(solution2(["Jane", "Kim"]))
