# 2022 KAKAKO BLIND 4.양궁대회

MAX_SCORE_DIFF = 0  #
ANSWER = [-1]  #


def check_promising(temp_target) -> bool:
    global ANSWER

    for i in range(10, -1, -1):
        if temp_target[i] > ANSWER[i]:
            return True
        elif temp_target[i] < ANSWER[i]:
            return False

    return False


def cal_score(ryan_win, reamin_arrows, info) -> None:
    global MAX_SCORE_DIFF, ANSWER

    ryan = 0  # 라이언 점수
    apeach = 0  # 어피치 점수
    temp_target = [0] * 11  # 현재 승패로 맞춰질 과녁

    for i in range(10):
        score = 10 - i
        if ryan_win[i]:  # 라이언이 이긴 경우
            ryan += score
            temp_target[i] = info[i] + 1  # 한발만 더 맞혀서 점수를 얻음
            reamin_arrows -= info[i] + 1  # 화살 수 감소
            if reamin_arrows < 0:  # 화살 없음 -> 불가능
                return
        elif not ryan_win[i] and info[i]:  # 결과가 Fasle인 경우라도 어피치가 1발이라도 맞춰야 점수 얻을 수 있음
            apeach += score

    # 남은 화살은 최적 경우를 위해서 0점에 몰빵
    if reamin_arrows:
        temp_target[10] += reamin_arrows

    # 조건 맞추기 - 같은 점수이면, 낮은 점수를 많이 맞힌쪽이 이김
    score_diff = ryan - apeach
    if MAX_SCORE_DIFF < score_diff:
        MAX_SCORE_DIFF = score_diff
        ANSWER = temp_target
    elif score_diff and MAX_SCORE_DIFF == score_diff:  # 점수차가 0인경우에는 어피치가 이긴것임
        if check_promising(temp_target):
            ANSWER = temp_target


def dfs(target, ryan_win, n, info) -> None:
    if target == 10:
        cal_score(ryan_win, n, info)
        return

    for rst_round in [True, False]:
        ryan_win.append(rst_round)
        dfs(target + 1, ryan_win, n, info)
        ryan_win.pop()


def solution(n, info) -> list:
    # n: 화살개수, info: 어피치 결과, 라운드: 10 (0점은 상관X이므로)
    # 해당 라운드 점수 얻는다 / 얻지 않는다.
    # 얻는 경우는 apeach + 1 / 얻x는 그냥 0
    # 가장 큰 점수차 - 어차피 2^10 완전탐색 할 것?
    # 먼저 승패 결과를 결정해두고 화살 사용후에 남은 화살은 0에 몰빵하는게 조건에 맞는듯
    # 못이기는 경우 -1 (화살이 모자름 등)

    global MAX_SCORE_DIFF, ANSWER

    dfs(0, [], n, info)  # 과녁 점수, 승/패 기록, 화살 수, 어피치 결과
    return ANSWER


n = 9
info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(n, info))

"""
    - 쉽게 생각했는데 꽤나 고생한 문제

    - 라이언의 (승/승x)를 나눠서 선택한 이후에 결과에 맞춰서 
      이기려면 어피치보다 한발 더, 그렇지 않으면 아예 0발을 쏴서 화살수를 아낀다.
      과녁의 총 점수의 개수가 11개 이므로 점수 카운팅이 안되는 0점을 제외하면 2^10로 완전탐색으로 해결할 수 있다. 

    - 남은 화살은 문제의 최적조건을 위해서 0점에다가 모두 사용한다. 

    - 점수 차이가 같을때의 조건 판단(check_promising())을 안해줘서 해맴
    
    - 이후에 ANSWER의 초기값이 [-1]인데 둘 사이의 점수차이가 0점인 경우를 제외하지 않아서 
      indexing error때문에 고생했다. ㅠ
"""