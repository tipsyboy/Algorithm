# https://www.acmicpc.net/problem/3015

import sys

input = sys.stdin.readline


N = int(input())
stack = []
ans = 0
for _ in range(N):
    now = int(input())
    cnt = 1

    while stack and stack[-1][0] <= now:
        height, cnt = stack.pop()
        if height == now:
            ans += cnt
            cnt += 1
        elif height < now:
            ans += cnt
            cnt = 1  #####

    if stack:
        ans += 1
    stack.append((now, cnt))

print(ans)


"""
3015. 오아시스 재결합

    - 거의 20번은 틀린듯.. 결국 해설봤음
      다른 언어였으면 큰 수 처리도 해줘야하고 쉽게 보고 덤볐다가 굉장히 까다로운 문제라는 것을 알게됨..

    - 포인트는 '두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.' -> or 에 집중해서 문제를 읽는 것과
      이때 동일한 키를 가진 사람들을 처리하는 방식이다. stack 안에는 단순 감소로만 유지하므로 이 과정이 굉장히 골머리가 아픔

    - 마지막으로 cnt를 초기화 해주지 않아서 (##### 부분) 5번은 더 틀린듯    
"""
