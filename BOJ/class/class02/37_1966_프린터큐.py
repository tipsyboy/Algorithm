import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())  # 자료 개수, target의 순서
    que = list(map(int, input().split()))  # 프린터 큐 안의 우선순위
    temp = [x for x in range(n)]
    temp[m] = "target"  # target
    idx = 1  # 출력 순서

    while True:
        if que[0] != max(que):
            que.append(que.pop(0))
            temp.append(temp.pop(0))
        else:
            if temp[0] != "target":
                que.pop(0)
                temp.pop(0)
                idx += 1
            else:
                print(idx)
                break
