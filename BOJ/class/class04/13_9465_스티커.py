import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    sticker[0][1] = sticker[0][1] + sticker[1][0]
    sticker[1][1] = sticker[1][1] + sticker[0][0]

    for i in range(2, n):
        sticker[0][i] = max(sticker[1][i-1], sticker[1][i-2]) + sticker[0][i]
        sticker[1][i] = max(sticker[0][i-1], sticker[0][i-2]) + sticker[1][i]

    print(max(sticker[0][-1], sticker[1][-1]))


"""
13. 9465 스티커 (Silver 2)
    - 첫 번째 생각은 리스트들에서 가장 큰 수만 greedy로 뽑아 내서 저장하고, 
      인접한 원소들을 없애는 방식이었으나, 약 10s간 더 생각하니까 아무리봐도 그리디는 아니었다. 
      테스트 케이스의 값이 이렇게 풀려서 살짝 현혹될뻔 했으나, max값 탐색할때도 시간 오래걸리고
      아무튼 패스

    - 두 번째는 단순 (0, 0), (1, 0) 두 점에서 시작해서 지그재그로 값을 더해 나가는 방법이었는데, 
      테스트 케이스에 부합하지 않았음. 이때, 세 번째 방법을 생각하게 됨

    - 세 번째 생각은 현재 i열의 값을 포함 하려고 할때, 이전 지그재그의 max값을 찾는 것이다. 
      말로 설명하기가 좀 그런데 i열을 포함하려고 할때 i-1열은 직접적인 영향력을 받게 되고 이에따라서
      i-2열도 영향을 받게 된다. 그 이전항을 i열과 직접 연관성이 없다. 따라서 i-3열 값까지는 최적값이 있다고 
      생각하고, i열의 값이 dp값에 포함되려고 할때, i-1열 값에 포함시킬 것인지, 아니면 i-1열을 포기하고 i-2열 값을 
      가져갈 것인지에 대해서만 생각해 주면된다.
    
      말로 풀기가 살짝 애매하지만 그려서 보면 바로 알 수 있었다. 

    - dp에서 바텀업 방식에 대해서는 현재 i항에 집중해서 현재 i항이 들어갈 수 있는가 없는가를
      중점적으로 보는게 맞는것 같다. 
"""
