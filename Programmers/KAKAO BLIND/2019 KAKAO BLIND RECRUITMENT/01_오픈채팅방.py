# https://school.programmers.co.kr/learn/courses/30/lessons/42888

from collections import defaultdict

MESSAGES = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}


def solution(record):
    nicknames = defaultdict(str)
    logs = []

    for r in record:
        command, *info = r.split()

        if command == "Leave":
            uid = info[0]
            logs.append((command, uid))
        else:
            uid, nickname = info[0], info[1]
            nicknames[uid] = nickname

            if command == "Enter":
                logs.append((command, uid))

    ans = []
    for log in logs:
        command, uid = log
        ans.append(f"{nicknames[uid]}{MESSAGES[command]}")

    return ans


print(
    solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    )
)


"""
오픈 채팅방

문제의 포인트
1. 문자열을 다룰 수 있는가? - 문자열 저장, 파싱
2. 문제 명령어에 의한 분기
3. 문제의 조건 record 개수 10_000, 닉네임의 길이 10 제한을 보고 완전탐색 유형으로 바로 생각할 수 있는가?
4. 해시맵 자료구조를 알고 입력, 수정 등 활용할 수 있는가? 
5. 문자열을 헤매이지 않고 깔끔하게 해결할 수 있는가?

---
- 문자열
- 자료구조
- 브루트 포스 
"""
