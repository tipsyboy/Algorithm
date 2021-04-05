import sys


def solution1(n, k):
    count = 0
    cnt = 1
    while True:
        print(f"[sol1] while문에 들어온 횟수: {cnt}")
        cnt += 1
        # n이 1이면 조건이므로 break
        if n == 1:
            break

        if n % k == 0:  # n이 k로 나누어 떨어지면 나누고
            n //= k
        else:  # 안되면 1을 뺀다.
            n -= 1

        count += 1

    return count


def solution2(n, k):
    count = 0
    cnt = 1

    while True:
        print(f"[sol2] while문에 들어온 횟수: {cnt}")
        cnt += 1

        # n에서 k로 나누어 떨어지는 수까지 가기 위해서 -1을 하는 과정
        target = (n // k) * k
        count += n - target
        n = target

        # 더 이상 나눌 수 없는 경우
        if n < k:
            break

        # 나누어 떨어져서 나누는 경우
        n //= k
        count += 1  # 나누는 경우는 1차시이므로 1 더해줌

    count += n - 1  # n을 1로 만들때까지

    return count


n, k = map(int, sys.stdin.readline().split())

print(solution1(n, k))
print(solution2(n, k))
