import sys
input = sys.stdin.readline

target = int(input())  # target number
m = int(input())  # 고장난 버튼의 수
button = set(map(str, input().split()))  # 고장난 버튼

# 1) +, - 버튼만을 사용해서 target number를 찾는 경우
rst = abs(target - 100)  # 채널의 시작 번호가 100

# 2) target보다 낮은 수에서 +를 누르면서 찾는 경우
for channel in range(target, -1, -1):  # 채널은 0번부터 있음
    flag = True  # 이중 for 탈출
    for num in str(channel):
        if num in button:
            flag = False
            break
    if flag:
        rst = min(rst, len(str(channel)) + target - channel)
        break

# 3) target보다 높은 수에서 -를 누르면서 찾는 경우
# target channel의 범위가 50만까지고 채널은 무한대 개수이므로 50만보다 높은 수의 채널에서 내리면서 찾는 경우가 이득일 때도 있다.
for channel in range(target, 1000001):
    flag = True
    for num in str(channel):
        if num in button:
            flag = False
            break
    if flag:
        rst = min(rst, len(str(channel)) + channel - target)
        break

print(rst)


"""
43. 1107 리모컨 (gold 5)
    - 굉장히 헤맸었던 문제, 처음의 생각은 target에서 고장난 버튼이 있으면 그 자리만 내림/올림해서 +/-하면서 찾아 내려고 했었다. 
      하지만 자리수에서 고장난 버튼만 수정하는 것보다 이득이 되는 상황이 분명히 존재했음.
      ex) target이 5457이고 5,6,7이 고장난 버튼이면 처음에 내 생각대로라면 4444 or 4448부터 찾거나 했어야 했지만 4999가 더 이득번호다. 
    
    - 때문에 굉장히 헤매다가 브루트포스 힌트를 얻어서 풀게 되었다. (브루트포스가 구현방법은 쉬워도 알아챌 때까지가 어려운듯....)
    
    - 최대 근접수에서 내리는 경우에 1000000까지의 범위수를 갖는 것은 target이 50만 범위를 갖고 있고 채널 수는 무한대기 때문에
      target의 max인 50만 보다 높은 곳에서 내려오는 것이 이득인 경우가 생기기 때문이다.
    
    - 추가로 다른사람들의 코드를 보니까 모든 수에 대해서 1000000범위의 수를 검증하던데 나는 위/아래에서 올라/내려가는 경우의 수를 나눠서 생각했고, 
      처음 찾는 수가 target에 가장 근사치인 수이기 때문에 바로 break를 걸고 루프를 탈출했다. 
      이렇게 처리했더니 많은 시간 감소가 있었다. (1400ms -> 500ms)
"""
