# https://www.acmicpc.net/problem/13414

import sys

input = sys.stdin.readline

K, L = map(int, input().split())

seq_dic = dict()
for i in range(L):
    num = input().rstrip()
    seq_dic[num] = i

seq_arr = sorted(seq_dic.items(), key=lambda x: x[1])[:K]
for i in range(len(seq_arr)):
    print(seq_arr[i][0])