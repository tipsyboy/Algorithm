# https://www.acmicpc.net/problem/1965

import sys
from bisect import bisect_left

input = sys.stdin.readline


n = int(input())
boxes = list(map(int, input().split()))
ans = [boxes[0]]
for i in range(1, n):
    if boxes[i] > ans[-1]:
        ans.append(boxes[i])
    else:
        ans[bisect_left(ans, boxes[i])] = boxes[i]

print(len(ans))

"""
1965. 상자넣기
    - LIS 입문으로 좋을것 같은 문제

    - bisect 모듈을 사용했다. 바퀴를 다시 만들지 말자
"""