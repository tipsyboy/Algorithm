


# N번 원판을 start에서 to로 옮긴다.
def move(N, start, to):
    print(f"{N}: {start} -> {to}")


# 판의 개수 N을 받아서 start에서 to까지 via를 거친다.
def hanoi(N, start, to, via):
    if N == 1:  # 만약 판의 개수가 하나면
        # move(1, start, to) # 하나의 판을 start 지점에서 to로 이동
        print(start, to)
        return

    hanoi(N-1, start, via, to)  # 가장 큰 N번 원판을 옮기기 위해서 N-1개의 원판을 via로 옮긴다.
    # move(N, start, to)
    print(start, to)
    hanoi(N-1, via, to, start)


N = int(input())  # 판의 개수 N
print(2 ** N - 1)
hanoi(N, '1', '3', '2')
