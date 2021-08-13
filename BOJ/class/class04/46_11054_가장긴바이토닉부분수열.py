import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
seq_reversed = list(reversed(seq))
dp = [1] * n
dp_r = [1] * n

for i in range(1, n):
    for j in range(i):
        # 정방향
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

        # 역방향
        if seq_reversed[i] > seq_reversed[j]:
            dp_r[i] = max(dp_r[i], dp_r[j] + 1)

dp_r.reverse()

for i in range(n):
    dp[i] = dp[i] + dp_r[i]

print(max(dp) - 1)


"""
46. 11054 가장 긴 바이토닉 부분수열 (Gold 3)
    - dp 문제이고, 문제 난이도에 비해서 어려운 점은 없는 편이다. 

    - 이전에 가장 긴 부분수열(LIS) 문제 응용으로 바이토닉 부분수열에서 감소하는 부분은 수열을 뒤에서부터 읽었을때, 증가하는 수열이 된다. 
      따라서, 받은 수열을 한번 뒤집어 주고 dp와 같은 방법으로 dp_r을 구한다. 
      이후에 다시 dp_r을 뒤집어서 되돌려주면 감소하는 부분수열의 길이가 되기 때문에 dp와 dp_r의 같은 index의 값을 더해주고
      i index의 값이 중복되므로 -1을 해서 마무리 해준다. 
"""