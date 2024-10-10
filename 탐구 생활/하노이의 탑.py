"""
# Last Modified. 2024.10.10 THU
# 하노이의 탑

"""


# 하노이의 탑 원반의 움직임을 출력한다.
def move(n: str, start: str, dest: str) -> None:
    print("%d번 원반을 %s에서 %s로 옮긴다." % (n, start, dest))


# 하노이의 탑의 {n번 원반}을 {start}에서 {via}를 통해서 {dest}로 옮긴다.
def hanoi_tower(n: int, start: str, via: str, dest: str) -> None:
    if n == 1:
        move(1, start, dest)
        return

    hanoi_tower(n - 1, start, dest, via)  # n번째 원반을 옮기기 위한, n-1을 이동하는 과정
    move(n, start, dest)  # n번째 원반을 옮기고
    hanoi_tower(n - 1, via, start, dest)  # n-1의 원반을 옮기기 위해 함수 재출발


k = int(input())
print("전체 이동 횟수: %d" % (2**k - 1))  # hanoi의 탑 일반항 유도를 통해 구함
hanoi_tower(k, "A", "B", "C")
