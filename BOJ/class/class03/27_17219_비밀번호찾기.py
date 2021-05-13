import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 사이트 수, m: 찾으려는 사이트 수
notepad = dict()

# 비밀번호 저장 하기
for _ in range(n):
    addr, password = input().split()
    notepad[addr] = password

# 비밀번호 찾기
for _ in range(m):
    addr = input().rstrip()

    print(notepad[addr])
