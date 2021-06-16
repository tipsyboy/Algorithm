import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

# 0: R, 1: G, 2: B
for i in range(1, n):
    # R로 끝나는 경우
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    # G로 끝나는 경우
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    # B로 끝나는 경우
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[-1]))


"""
09. 1149 RGB 거리 (Silver 1)
    - 기초적인 DP 문제, 하지만 꽤 오래 걸려서 풀었다..

    - 문제의 조건에 따르면, 결국 이전 집과 색이 같지 않으면 조건을 만족한다. 

    - 따라서 매 상황마다 n번째 집이 R/G/B로 끝나는 경우로 생각하고 이전 회차 경우의 수에서
      이번에 올 R/G/B가 아닌 색중에 최솟값을 선택 하는 방식으로 진행한다. 

      ex) n번째 R집이 마지막에 오는 경우라고 하면, n번째 집 R값이 마지막에 오는 값이라고 하고,
          이전의 G/B가 마지막에 오는 집에서 최솟값을 선택한다. 
          즉, ~~~~~G와 ~~~~~B중에 최솟값을 선택해서 ~~~~~~GR 또는 ~~~~~~~~BR을 만드는 것이다. 
"""
