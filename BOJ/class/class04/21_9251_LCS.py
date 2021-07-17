import sys
input = sys.stdin.readline

str_x = input().rstrip()
str_y = input().rstrip()

common = [[0] * (len(str_y) + 1) for _ in range(len(str_x) + 1)]

for i in range(1, len(str_x) + 1):
    for j in range(1, len(str_y) + 1):
        if str_x[i-1] == str_y[j-1]:
            common[i][j] = common[i-1][j-1] + 1
        else:
            common[i][j] = max(common[i-1][j], common[i][j-1])

print(common[-1][-1])


"""
21. 9251 LCS(Longest Common Subsequence) (Gold 5)
    - dp 문제로 0-1 냅색 문제랑 거의 비슷한 유형이었다. 
      냅색 공부했을 때처럼 점화식을 세워서 해결했다. 
      이번처럼 dp 문제를 풀때는 현재 항 i에 집중해서 꼭 점화식을 세워서 푸는 버릇을 들여야겠다. 
    
    - 2차원 배열을 선언해 둔 후에 str_x의 현재항 i와 str_y의 현재항 j index를 비교한다. 
      연속되는 부분수열이 아니기 때문에, 현재 i, j항에서 들어오는 값(문자)를 비교하면서
      같으면 이전 수열에 포함하기 때문에 이전 값에서 +1 해주는 것이고,
      다르다면 이전까지 최장 부분 수열을 그대로 가져다가 쓰는 것이기 때문에 (i-1, j) (i, j-1) 값중에서 큰 값을 선택한다. 

    - dp는 현재항 i에 집중해서 이전 값들이 최적 조건에 부합한다는 생각을 갖고 접근하자!
"""
