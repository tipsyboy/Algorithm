def get_alphabet_dist(target):
    return min(ord(target) - ord("A"), ord("Z") - ord(target) + 1)


def solution(name):
    # 주어진 문자열 name을 전부 탐색해야함 - 왜 why? 당연히 모든 알파벳 값을 변경해야 하니까
    # 때문에 문자열의 길이를 선형탐색 경우가 최초 최소값으로 (문자열의 길이 - 1)이다.
    min_value = len(name) - 1
    count = 0

    # 결국에 그리디한 방법은 최적해를 뽑아내지 못함 앞뒤로 탐색하면서 턴해야함
    # idx는 축이 되고 idx로부터 turn까지 왼쪽, 오른쪽으로 회전한다.
    for idx, char in enumerate(name):
        count += get_alphabet_dist(char)

        turn = idx + 1
        while turn < len(name) and name[turn] == "A":
            turn += 1

        # 오른쪽 이동
        right = idx * 2 + len(name) - turn
        # 왼쪽 이동
        left = (len(name) - turn) * 2 + idx

        min_value = min(min_value, left, right)

    count += min_value

    return count


# "OAOAAAAAOAO",
names = [
    "JEROEN",
    "BBAAAAAAABBBB",
    "BBBBAAAAAAABB",
    "ABAAAA",
    "AABBAAAAAAB",
    "ABABAAAABB",
]
for name in names:
    print(solution(name))
