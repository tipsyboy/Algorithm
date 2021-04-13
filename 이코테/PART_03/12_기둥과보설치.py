# 2020 카카오 블라인드 1차
# 기둥과 보 설치


# demo 버전 빌딩을 받아서 현재 빌딩이 가능한 건축물인가를 판단한다.
def possible_demo(building):
    for demo in building:
        x, y, stuff = demo

        # 건축물이 기둥인 경우
        if stuff == 0:
            if (
                y == 0  # 땅에 기둥을 설치
                or [x, y - 1, 0] in building  # 기둥위에 기둥을 설치
                or [x - 1, y, 1] in building  # 보 위에 기둥을 설치
                or [x, y, 1] in building  # 보 위에 기둥을 설치
            ):
                continue

            return False

        # 건축물이 보인 경우
        else:
            if (
                [x, y - 1, 0] in building  # 기둥 위에 보를 설치
                or [x + 1, y - 1, 0] in building  # 기둥 위에 보를 설치
                or ([x - 1, y, 1] in building and [x + 1, y, 1] in building)  # 보와 보를 연결
            ):
                continue

            return False

    return True  # 가능한 건축물이면 True


def solution(n, build_frame):
    building = []  # 건축물을 저장한다.

    # 빌드 프레임에서 하나씩 커맨드를 꺼내서
    for frame in build_frame:
        x, y, stuff, command = frame

        # 건축/삭제 판단 하고
        # list(건축물 저장)에 추가 또는 삭제를 진행한다.
        if command == 1:  # 건물을 설치
            building.append([x, y, stuff])
            # 그 건축물이 존재할 수 있는지 검사한 후에
            if not possible_demo(building):
                building.remove([x, y, stuff])  # 존재 할 수 없는 건축물이면 list(건축물 저장)에서 뺀다.
        else:  # 건물을 삭제하는 경우 command == 0
            building.remove([x, y, stuff])
            # 건축물 존재 가능 여부
            if not possible_demo(building):
                building.append([x, y, stuff])  # 가능하지 않으면 다시 설치

    return sorted(building)


#####
# set() 자료형으로 바꾸면
# 탐색과 추가, 삭제에 걸리는 시간이 O(1)이기 때문에 훨씬 속도가 빨라진다.


# # 2020 카카오 블라인드 1차
# # 기둥과 보 설치


# # demo 버전 빌딩을 받아서 현재 빌딩이 가능한 건축물인가를 판단한다.
# def possible_demo(building):
#     for demo in building:
#         x, y, stuff = demo

#         # 건축물이 기둥인 경우
#         if stuff == 0:
#             if (
#                 y == 0  # 땅에 기둥을 설치
#                 or (x, y - 1, 0) in building  # 기둥위에 기둥을 설치
#                 or (x - 1, y, 1) in building  # 보 위에 기둥을 설치
#                 or (x, y, 1) in building  # 보 위에 기둥을 설치
#             ):
#                 continue

#             return False

#         # 건축물이 보인 경우
#         else:
#             if (
#                 (x, y - 1, 0) in building  # 기둥 위에 보를 설치
#                 or (x + 1, y - 1, 0) in building  # 기둥 위에 보를 설치
#                 or ((x - 1, y, 1) in building and (x + 1, y, 1) in building)  # 보와 보를 연결
#             ):
#                 continue

#             return False

#     return True  # 가능한 건축물이면 True


# def solution(n, build_frame):
#     building = set()  # 건축물을 저장한다.

#     # 빌드 프레임에서 하나씩 커맨드를 꺼내서
#     for frame in build_frame:
#         x, y, stuff, command = frame

#         # 건축/삭제 판단 하고
#         # list(건축물 저장)에 추가 또는 삭제를 진행한다.
#         if command == 1:  # 건물을 설치
#             building.add((x, y, stuff))
#             # 그 건축물이 존재할 수 있는지 검사한 후에
#             if not possible_demo(building):
#                 building.remove((x, y, stuff))  # 존재 할 수 없는 건축물이면 list(건축물 저장)에서 뺀다.
#         else:  # 건물을 삭제하는 경우 command == 0
#             building.remove((x, y, stuff))
#             # 건축물 존재 가능 여부
#             if not possible_demo(building):
#                 building.add((x, y, stuff))  # 가능하지 않으면 다시 설치

#     return sorted(list(building))
