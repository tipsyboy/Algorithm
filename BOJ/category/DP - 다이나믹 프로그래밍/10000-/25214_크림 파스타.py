import sys

input = sys.stdin.readline
INF = float("inf")

N = int(input())
arr = list(map(int, input().split()))

minv_in_arr = INF
maxv = 0
ans = []
for i in range(N):
    if arr[i] < minv_in_arr:
        minv_in_arr = arr[i]
    else:
        maxv = max(maxv, arr[i] - minv_in_arr)

    ans.append(maxv)
print(*ans)


"""
25214. 크림 파스타
    - 문제의 제목과는 전혀 상관 없는 문제 ㅋㅋ...
    
    - list의 i번째 까지의 minv를 저장하면서 값을 추가해가면 된다. O(n)?
    
    - list의 앞의 내용을 전부 비교하면서 가면 N^2으로 당연히 TLE다
"""