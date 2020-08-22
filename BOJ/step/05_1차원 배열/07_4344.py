import sys

N = int(sys.stdin.readline())

for i in range(N):
    score = list(map(int, sys.stdin.readline().split()))  # 0번 idx는 학생 수
    avg = (sum(score) - score[0]) / score[0]
    count = 0

    for i in range(1, score[0]+1):
        if score[i] > avg:
            count += 1

    print(str("%.3f" % (count/score[0]*100)) + "%")  # 소수점 자리수 출력하기
