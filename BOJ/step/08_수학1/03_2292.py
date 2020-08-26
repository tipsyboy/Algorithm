import sys

N = int(sys.stdin.readline())
layer = 1

while True:
    if N <= (3*layer)*(layer-1) + 1:  # 계차수열의 일반항
        print(layer)
        break
    else:
        layer += 1
