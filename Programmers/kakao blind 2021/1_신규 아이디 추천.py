def solution(new_id):
    # 1. 대문자 -> 소문자 변환
    # 2. 허용 문자 이외의 모든 문자를 삭제
    # 3. '.' 마침표가 연속되면 하나로 치환
    # 4. new_id가 빈 문자열이면 "a"를 대입
    # 5. id가 16자 이상이면 15자를 제외 모두 제거 - 제거후 .마침표가 끝에있다면 .마침표를 제거
    # 6. new_id길이가 2자 이하면 new_id의 길이가 3이 될때까지 마지막 문자를 붙임
    special = {"-", "_", "."}
    new_id = new_id.lower()

    answer = ""
    for char in new_id:
        if char.isalpha() or char.isdigit():
            answer += char
            continue

        if char not in special:
            continue

        if not answer or char == "." and answer[-1] != ".":
            answer += "."
            continue

        answer += char

    if answer[0] == ".":
        answer = answer[1:]
    if answer[-1] == ".":
        answer = answer[:-1]

    if not answer:
        answer = "a"

    if len(answer) > 15:
        answer = answer[:14]

    if answer[-1] == ".":
        answer = answer[:-1]

    if len(answer) < 3:
        last_char = answer[-1]
        answer += last_char * (3 - len(answer))

    print(answer)
    return answer


new_id = "z-+.^."
solution(new_id)