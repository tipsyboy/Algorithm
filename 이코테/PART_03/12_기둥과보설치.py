import sys

input = sys.stdin.readline


def possible(building):
    for x, y, a in building:
        # 구조물이 기둥
        if a == 0:
            if (
                y == 0
                or (x, y - 1, 0) in building
                or (x - 1, y, 1) in building
                or (x, y, 1) in building
            ):
                continue
            return False
        # 구조물이 보
        elif a == 1:
            if (
                (x, y - 1, 0) in building
                or (x + 1, y - 1, 0) in building
                or ((x - 1, y, 1) in building and (x + 1, y, 1) in building)
            ):
                continue

            return False

    return True


def solution(n, build_frames):
    building = set()

    for frame in build_frames:
        x, y, a, b = frame  # 이번 프레임을 받아온다.

        # 구조물을 설치
        if b == 1:
            building.add((x, y, a))

            # 구조물이 가능하지 않으면 다시 원상 복구
            if not possible(building):
                building.remove((x, y, a))
        # 구조물을 제거
        elif b == 0:
            if (x, y, a) in building:
                building.remove((x, y, a))

                # 구조물이 가능하지 않으면 다시 원상 복구
                if not possible(building):
                    building.add((x, y, a))

    rst = []
    for data in building:
        rst.append(list(data))

    rst.sort(key=lambda x: (x[0], x[1], x[2]))

    return rst


n = 5
build_frames = [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 0, 1],
    [2, 2, 1, 1],
    [5, 0, 0, 1],
    [5, 1, 0, 1],
    [4, 2, 1, 1],
    [3, 2, 1, 1],
]

print(solution(n, build_frames))


"""
12. 기둥과 보 설치 
    - 기둥, 보의 설치 정보를 어떻게 저장할 것인가?
      
      기둥과 보는 설치 방향이 정해져 있기 때문에 (시작하는 위치 좌표, 구조물)를 가지고 있으면 된다.

    - 차례로 현재 설치/삭제될 구조물을 추가/제거한 후에 가능한지에 대해서 전부 검사한다. 

    - set() 자료형 사용의 정당성
      
      처음엔 set()은 순서가 보장되지 않기 때문에 설치 순서에 따라서 결과물이 달라지는 이번 문제에 대해서 사용할 수 없을 것이라고 생각했으나,
      build_frames 자체는 순서대로 들어오고, 그때마다 현재 건물의 상태에 현재 구조물을 추가/제거 할 수 있느냐만 검사하는 것이기 때문에
      set()을 사용할 수 있다.
"""
