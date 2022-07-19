directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def solution(dirs):
    visited = set()

    ans = 0
    x, y = 0, 0
    for com in dirs:
        nx, ny = x + directions[com][0], y + directions[com][1]

        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        if (x, y, nx, ny) not in visited:
            ans += 1
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))

        x, y = nx, ny

    return ans


"""
방문 길이.
    - 처음엔 임의의 좌표 (x, y)에 대해서 위/아래/왼/오른쪽의 접근만 판단해서 
      각각 4, 3, 2, 1로 주고 비트마스크를 통해서 방문 처리를 시행 했지만, i -> j의 경로와 j -> i의 경로가 같으므로 실패

    - set()을 쓰지 않고 해결하려다가.. set으로 그냥 마무리
"""